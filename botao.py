import pygame
import random
import time
from os import path

img_dir = path.join(path.dirname(__file__), 'img')


FPS = 60 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
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

        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
    # Metodo que atualiza a posição da navinha
    def update(self):
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

pygame.init()
pygame.mixer.init()
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OSU2")
clock = pygame.time.Clock()
background = pygame.image.load(path.join(img_dir, 'background.jpg')).convert()
background_rect = background.get_rect()
all_sprites = pygame.sprite.Group()
botoes = pygame.sprite.Group()
botao = Mob()
tamanho=200
timing=circulo()
all_sprites.add(botao)
all_sprites.add(timing)
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
                if pygame.mouse.get_pos()[0]<botao.posicao()[0]+25 and pygame.mouse.get_pos()[0]>botao.posicao()[0]-25 and pygame.mouse.get_pos()[1]>botao.posicao()[1]-25 and pygame.mouse.get_pos()[1]<botao.posicao()[1]+25:
                    if tamanho>30 and tamanho<70:
                        botao.kill()
                        timing.kill()
        if tamanho>35:
            tamanho-=3
            timing.update()

        
        # Depois de processar os eventos.
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    
    pygame.quit()


