import pygame


def main():
    pais = input("Selecione um país: Alemanha(A)/Guiné(G)/Laos(L) ")
    if(pais == "A" or pais == "a"):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 200), 0)
        pygame.draw.rect(screen, (255, 0, 0), (0, 200, 600, 200), 0)
        pygame.draw.rect(screen, (255, 255, 0), (0, 400, 600, 200), 0)
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
    elif(pais == "G" or pais == "g"):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 200, 600), 0)
        pygame.draw.rect(screen, (255, 255, 0), (200, 0, 200, 600), 0)
        pygame.draw.rect(screen, (0, 148, 96), (400, 0, 200, 600), 0)
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
    elif(pais == "L" or pais == "l"):
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 600, 150), 0)
        pygame.draw.rect(screen, (0, 0, 255), (0, 150, 600, 300), 0)
        pygame.draw.rect(screen, (255, 0, 0), (0, 450, 600, 150), 0)
        pygame.draw.circle(screen, (255, 255, 255), (300, 300), 90)
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
    else:
        print('Opção inválida')


main()

