#Felipe Dantas Tavares - 32080549
#Henrique Lima Araújo - 32091702
import pygame
import random


class Quadrado():
    def __init__(self):
        self.altura = 0
        self.largura = 0
        self.cor = (0, 0, 0)
        self.posx = 0
        self.posy = 0

    def sorteiacor(self):
        self.cor = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
        return self.cor

    def sorteiax(self):
        self.posx = random.randrange(0,301)
        return self.posx

    def sorteiay(self):
        self.posy = random.randrange(0,301)
        return self.posy


def main():
    q = Quadrado()
    q.largura = 250
    q.altura = 250
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill((255, 255, 255))
    while(q.altura >= 1 and q.largura >= 1):
        pygame.draw.rect(screen, q.sorteiacor(), (q.sorteiax(), q.sorteiay(), q.largura, q.altura), 0)
        q.largura = q.largura/2
        q.altura = q.altura/2
    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.quit()


main()

