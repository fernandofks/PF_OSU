import pygame
from os import path
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
DKGREEN = (0, 100, 0)

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), "snd")
fnt_dir = path.join(path.dirname(__file__), "font")
class circulo(pygame.sprite.Sprite):
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "circulo.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (tamanho, tamanho))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = botao.posicao()[0]
        # Sorteia um lugar inicial em y
        self.rect.centery = botao.posicao()[1]
    # Metodo que atualiza a posição da navinha
    def update1(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = botao.posicao()[0]
        self.rect.centery = botao.posicao()[1]
        mob_img = pygame.image.load(path.join(img_dir, "circulo.png")).convert()
        self.image = pygame.transform.scale(mob_img, (tamanho, tamanho))
        self.image.set_colorkey(BLACK)


class Mob(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "botaoup.jpg")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = random.randrange(WIDTH - 100)
        # Sorteia um lugar inicial em y
        self.rect.centery = random.randrange(HEIGHT - 100)

        # Melhora a colisão estabelecendo um raio de um circulo

    def posicao(self):
        return self.rect.centerx, self.rect.centery
class Player(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the player, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(path.join(img_dir, "Pointer.png")).convert()
        self.image.set_colorkey(BLACK)       

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    # Update the position of the player
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list, just like we'd fetch letters out
        # of a string.
        # NOTE: If you want to keep the mouse at the bottom of the screen, just
        # set y = 380, and not update it with the mouse position stored in
        # pos[1]
        x = pos[0]
        y = pos[1]

        # Set the attribute for the top left corner where this object is
        # located
        self.rect.centerx = x
        self.rect.centery = y

pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #pygame.FULLSCREEN)

# Don't display the mouse pointer
pygame.mouse.set_visible(False)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h
# This is a list of 'sprites.' Each sprite in the program (there is only 1) is
# added to this list. The list is managed by a class called 'Group.'
all_sprites_list = pygame.sprite.Group()
tamanho=200
botao=Mob()
timing=circulo()
all_sprites_list.add(timing)
all_sprites_list.add(botao)
# This represents the ball controlled by the player
player = Player()
#screen.fill(BLACK)
# Add the ball to the list of player-controlled objects
all_sprites_list.add(player)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.collide_circle(player,botao):
                    if tamanho>30 and tamanho<70:
                        botao.kill()
                        timing.kill()
    if tamanho>35:
        tamanho-=5
        timing.update1()

    all_sprites_list.update()
    #limpa a tela depois desenha
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(144)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
