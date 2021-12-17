#Este programa exibe flocos de neve caindo
import pygame
import random
# Initialize the game engine
pygame.init()
PRETO = [0, 0, 0]
BRANCO = [255, 255, 255]
# Set the height and width of the screen
SIZE = [420, 323]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Flocos de Neve")
fundo = pygame.image.load ("fundoNeve.jpg")
# Cria lista vazia
snow_list = []
# Adiciona 50 posições aleatórias na lista, onde cairão os flocos de neve
for i in range(50):
 x = random.randrange(0, 420)
 y = random.randrange(0, 323)
 snow_list.append([x, y])
clock = pygame.time.Clock()
# Game loop
done = False
while not done:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   done = True
 screen.blit(fundo, (0,0))
 # Processa cada ponto adicionado na lista
 for i in range(len(snow_list)):
  #exibe um floco de neve na posição correspondente
  pygame.draw.circle(screen, BRANCO, snow_list[i], 2)
  # movimenta o floco de neve um pixel abaixo
  snow_list[i][1] += 1
  # Verifica se o floco de neve saiu dos limites da tela
  if snow_list[i][1] > 420:
   # posiciona floco de neve antes do início da tela
   y = random.randrange(-50, -10)
   snow_list[i][1] = y
   # Determina nova posição
   x = random.randrange(0, 420)
   snow_list[i][0] = x
 pygame.display.flip()
 clock.tick(40)
pygame.quit()