import pygame, time
# definindo as cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
# definindo outras constantes do jogo
LARGURAJANELA = 500
ALTURAJANELA = 400
# definindo a função mover()
def mover(f1, dim_janela):
 borda_esquerda = 0
 borda_superior = 0
 borda_direita = dim_janela[0]
 borda_inferior = dim_janela[1]
 if f1['objRect'].top < borda_superior or f1['objRect'].bottom > borda_inferior:
  # figura atingiu o topo ou a base da janela
  f1['vel'][1] = -f1['vel'][1]
 if f1['objRect'].left < borda_esquerda or f1['objRect'].right > borda_direita:
  # figura atingiu o lado esquerdo ou direito da janela
  f1['vel'][0] = -f1['vel'][0]
 f1['objRect'].x += f1['vel'][0]
 f1['objRect'].y += f1['vel'][1]
# inicializando módulos de pygame
pygame.init()
# criando a janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Animação')
# criando a figura
f1 = {'objRect': pygame.Rect(200, 200, 20, 20), 'cor': VERDE, 'vel':
[5,5]}
deve_continuar = True
# loop do jogo
while deve_continuar:
# checando se ocorreu um evento QUIT
 for evento in pygame.event.get():
  if evento.type == pygame.QUIT:
   deve_continuar = False
 # preenchendo o fundo com a cor preta
 janela.fill(PRETO)
 # mudando a posição da figura
 mover(f1, (LARGURAJANELA, ALTURAJANELA))
 # desenhando a figura na janela
 pygame.draw.ellipse(janela, f1['cor'], f1['objRect'])
 # atualizando na tela tudo o que foi desenhado
 pygame.display.update()
 time.sleep(0.02)
pygame.quit()