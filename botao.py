import pygame
import random
import time
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 480 
HEIGHT = 600 
FPS = 60 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Mob(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "botaoup.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (50, 50))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def posicao(self):
        return self.rect.x, self.rect.y
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OSU2")
clock = pygame.time.Clock()
background = pygame.image.load(path.join(img_dir, 'background.jpg')).convert()
background_rect = background.get_rect()
all_sprites = pygame.sprite.Group()
botoes = pygame.sprite.Group()
botao = Mob()
all_sprites.add(botao)
botoes.add(botao)

try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0]<botao.posicao()[0]+50 and pygame.mouse.get_pos()[0]>botao.posicao()[0] and pygame.mouse.get_pos()[1]>botao.posicao()[1] and pygame.mouse.get_pos()[1]<botao.posicao()[1]+50:
                    botao.update()
        # Depois de processar os eventos.
    
 
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    
    pygame.quit()


