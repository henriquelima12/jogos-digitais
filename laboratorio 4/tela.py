#Henrique Lima Araújo - 32091702

import pygame, time
from random import randint

def sorteiacor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    cor = (r, g, b)
    return cor

def mover(f1, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if f1['objRect'].top < borda_superior or f1['objRect'].bottom > borda_inferior:
        f1['vel'][1] = -f1['vel'][1]
        f1['cor'] = sorteiacor()
    if f1['objRect'].left < borda_esquerda or f1['objRect'].right > borda_direita:
        f1['vel'][0] = -f1['vel'][0]
        f1['cor'] = sorteiacor()
    f1['objRect'].x += f1['vel'][0]
    f1['objRect'].y += f1['vel'][1]

pygame.init()
LARGURA = 600
ALTURA = 400
screen = pygame.display.set_mode((LARGURA, ALTURA))
fundo = pygame.image.load ("paisagem.jpg")
cachorro = pygame.image.load ("dog.jpg")
f1 = {'objRect': pygame.Rect(200, 200, 20, 20), 'cor': sorteiacor(), 'vel': [5, 5]}

jogoAtivo = True
while jogoAtivo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAtivo = False
    screen.blit(fundo, (0, 0))
    screen.blit(cachorro, pygame.mouse.get_pos())
    mover(f1, (LARGURA, ALTURA))
    pygame.draw.ellipse(screen, f1['cor'], f1['objRect'])
    pygame.display.update()
    time.sleep(0.01)
pygame.quit()
