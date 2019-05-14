import pygame
from os import path
import random
import time
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
i=0
d={}        
class Botao(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,n):
        
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
        
        self.n = n

        # Melhora a colisão estabelecendo um raio de um circulo

    def posicao(self):
        return self.rect.centerx, self.rect.centery
    def update(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0]<self.posicao()[0]+25 and pygame.mouse.get_pos()[0]>self.posicao()[0]-25 and pygame.mouse.get_pos()[1]>self.posicao()[1]-25 and pygame.mouse.get_pos()[1]<self.posicao()[1]+25:
                if d["circulo{0}".format(self.n)].tamanho>30 and d["circulo{0}".format(self.n)].tamanho<70:
                    self.kill()

class Circulo(pygame.sprite.Sprite):
    tamanho=200
    
    def __init__(self, n):
        self.n=n
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "circulo.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (self.tamanho, self.tamanho))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        self.rect.centerx = d["botao{0}".format(self.n)].posicao()[0]
        self.rect.centery = d["botao{0}".format(self.n)].posicao()[1]
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.centerx =d["botao{0}".format(self.n)].posicao()[0]
        self.rect.centery = d["botao{0}".format(self.n)].posicao()[1]
        mob_img = pygame.image.load(path.join(img_dir, "circulo.png")).convert()
        if self.tamanho>30:
            self.tamanho-=5
            self.image = pygame.transform.scale(mob_img, (self.tamanho, self.tamanho))
            self.image.set_colorkey(BLACK)
            if d["circulo{0}".format(self.n)].tamanho>30 and d["circulo{0}".format(self.n)].tamanho<70:
                self.kill()

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
# This represents the ball controlled by the player
player = Player()
all_sprites_list.add(player)
#screen.fill(BLACK)
# Add the ball to the list of player-controlled objects
tempo=[1.00, 5.00]
all_botoes=pygame.sprite.Group()
all_circulos=pygame.sprite.Group()
contador=0
# -------- Main Program Loop -----------
while not done:
    contador+=1
    if contador%60==0:
        a=Botao(i)
        all_botoes.add(a)
        d["botao{0}".format(i)]=a
        all_botoes.add(a)
        b=Circulo(i)
        all_circulos.add(b)
        d["circulo{0}".format(i)]=b
        i+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    all_botoes.update()
    all_circulos.update()
    player.update()
    #limpa a tela depois desenha
    screen.fill(BLACK)
    all_botoes.draw(screen)
    all_circulos.draw(screen)
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
pygame.quit()
