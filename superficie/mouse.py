import pygame, time
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
ROSA = (253, 147, 226)
LARGURAJANELA = 500
ALTURAJANELA = 400
pygame.init()
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Movendo com o mouse')
relogio = pygame.time.Clock()
ret = pygame.Rect(10, 10, 45, 45)
ret2 = pygame.Rect(50, 50, 80, 50)
deve_continuar = True

# loop do jogo
while deve_continuar:
 # checando se ocorreu um evento QUIT
 for evento in pygame.event.get():
     if evento.type == pygame.QUIT:
        deve_continuar = False
 # ao clicar o mouse, a figura se posiciona na parte central da tela
 if evento.type == pygame.MOUSEBUTTONDOWN:
     pygame.mouse.set_pos(250, 200)
 relogio.tick(30)
 janela.fill(PRETO)
 # o quadrado acompanha o mouse
 (ret.left, ret.top) = pygame.mouse.get_pos()
 ret.left -= int(ret.width / 2)
 ret.top -= int(ret.height / 2)
 pygame.draw.rect(janela, VERDE, ret)
 pygame.draw.rect(janela, ROSA, ret2)
 pygame.display.update()

 time.sleep(0.02)
pygame.quit()
