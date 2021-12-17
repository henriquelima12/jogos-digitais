#Henrique Lima Araújo - 32091702

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption("Estrada")

background = "pista.png"
imagem = "carro.png"
imagem_invertida = "carro_invertido.png"
pista = pygame.image.load(background)
carro = pygame.image.load(imagem)
carro_invertido = pygame.image.load(imagem_invertida)

red = (255,0,0)
white = (255,255,255)
my_font = pygame.font.SysFont("arial", 40, bold=True, italic=False)
superficie = my_font.render("GAME OVER", True, red, white)

x = 0
y = 125

x1 = 370
y1 = 335

JogoAtivo = True
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
    screen.blit(pista, (0, 0))
    if x < 960 and y == 125:
        screen.blit(carro, (x, y))
        pygame.display.update()
        x += 10
        pygame.time.delay(25)
    if x == 960 or x == 0:
        y += 240
    if y == 365:
        screen.blit(carro_invertido, (x, y))
        pygame.display.update()
        x -= 10
        pygame.time.delay(25)
    if y == 605:
        screen.blit(carro, (x, y))
        pygame.display.update()
        x += 10
        pygame.time.delay(25)
    if x == 960 and y == 605:
        screen.blit(superficie, (x1, y1))
        pygame.display.flip()

pygame.quit()