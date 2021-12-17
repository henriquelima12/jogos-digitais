import pygame, time
AMARELO = (248, 250, 197)
AZUL = (53, 72, 242)
ROSA = (253, 147, 226)
LARGURAJANELA = 400
ALTURAJANELA = 200

pygame.init()
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
#gameIcon = pygame.image.load('icone.png')
#pygame.display.set_icon(gameIcon)
pygame.display.set_caption('Clica e solta')
relogio = pygame.time.Clock()

#define as superficies
ret = pygame.Rect(10, 10, 50, 50)
ret2 = pygame.Rect(340, 10, 50, 50)

deve_continuar = True
click = 0
# loop do jogo
while deve_continuar:
 relogio.tick(150)
 for evento in pygame.event.get():
     if evento.type == pygame.QUIT:
        deve_continuar = False
     if evento.type == pygame.MOUSEBUTTONDOWN:
        click = 1
     elif evento.type == pygame.MOUSEBUTTONUP:
        click = 0
 janela.fill(AMARELO)

 if click == 1:
     x, y = pygame.mouse.get_pos()
     if (x >= ret.left and x <= ret.right) and (y >= ret.top and y <= ret.bottom):
         (ret.left, ret.top) = pygame.mouse.get_pos()
         ret.left -= int(ret.width / 2)
         ret.top -= int(ret.height / 2)
     if (x >= ret2.left and x <= ret2.right) and (y >= ret2.top and y <= ret2.bottom):
         (ret2.left, ret2.top) = pygame.mouse.get_pos()
         ret2.left -= int(ret2.width / 2)
         ret2.top -= int(ret2.height / 2)
 pygame.draw.rect(janela, AZUL, ret)
 pygame.draw.rect(janela, ROSA, ret2)

 pygame.display.update()
pygame.quit()