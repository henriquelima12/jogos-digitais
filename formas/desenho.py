import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill((0, 0, 255))
    pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 3)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 3)
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 3)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 3)
    pygame.draw.circle(screen, (255, 255, 0), (300, 300), 30)
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()


main()