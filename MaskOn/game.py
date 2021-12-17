#Felipe Dantas - 32080549
#Fernando Barreto - 32047568
#Henrique Lima - 32091702
#Lucas Lima – 32020724

import pygame, sys
from pygame.locals import *
from sys import exit
import os
from random import choice

pygame.init()
pygame.mixer.init()
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')
LARGURA = 640
ALTURA = 500
BRANCO = (255, 255, 255)
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Mask On')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'personagem.png')).convert_alpha()
som_fundo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'Future - Mask Off (Official Instrumental)_128k.mp3'))
som_fundo.set_volume(0.3)
som_fundo.play(-1)
som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jump_sound.wav'))
som_pulo.set_volume(0.3)
som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'game_over.wav'))
som_colisao.set_volume(0.3)
som_mask = pygame.mixer.Sound(os.path.join(diretorio_sons, 'coin.wav'))
som_mask.set_volume(0.3)
fundo = pygame.image.load ("imagens/cidade4.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
fontLogo = pygame.font.SysFont('Comic Sans MS', 60)
font = pygame.font.SysFont('Comic Sans MS', 40)
fontInstruction = pygame.font.SysFont('Comic Sans MS', 25)
anotherFont = pygame.font.SysFont('Comic Sans MS', 30)
mainClock = pygame.time.Clock()
escolha_obstaculo = choice([0, 1, 2, 3])
pontos = 0
clock = 40
soundActive = True
recorde = 0


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_personagem = []
        for i in range(6):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imagens_personagem.append(img)
        self.index_lista = 0
        self.image = self.imagens_personagem[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = ALTURA - 64 - 96
        self.rect.topleft = (100, self.pos_y_inicial)
        self.rect.center = (80, 420)
        self.pulo = False

    def pular(self):
        global soundActive, som_pulo
        self.pulo = True
        if soundActive == True:
            som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial
        if self.index_lista > 5:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_personagem[int(self.index_lista)]


class Virus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagens/virus2.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (LARGURA, ALTURA - 80)
        self.rect.x = LARGURA

    def update(self):
        if self.escolha == 0 or self.escolha == 2 or self.escolha == 3:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= 10


class Mask(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagens/mask.png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (LARGURA, 300)
        self.rect.x = LARGURA

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= 10


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagens/base.png')
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 64
        self.rect.x = pos_x * 64

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10

todas_as_sprites = pygame.sprite.Group()

personagem = Personagem()
todas_as_sprites.add(personagem)

virus = Virus()
todas_as_sprites.add(virus)

mask = Mask()
todas_as_sprites.add(mask)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(virus)

mascaras = pygame.sprite.Group()
mascaras.add(mask)

for i in range(LARGURA*2//64+1):
    chao = Chao(i)
    todas_as_sprites.add(chao)
    chao1 = pygame.sprite.Group()
    chao1.add(chao)

relogio = pygame.time.Clock()


def main_menu():
    click = False
    global soundActive, som_fundo
    while True:
        tela.fill((0, 0, 0))
        tela.blit(fundo, (0, 0))
        title = fontLogo.render("MASK ON", True, (0, 0, 0))
        tela.blit(title, (LARGURA/2 - title.get_width()/2, 20))
        mx, my = pygame.mouse.get_pos()
        start = font.render("JOGAR", True, (0, 0, 0))
        getStart = tela.blit(start, (LARGURA/2 - start.get_width()/2, 140))
        opt = font.render("INSTRUÇÕES", True, (0, 0, 0))
        getOptions = tela.blit(opt, (LARGURA/2 - opt.get_width()/2, 210))
        ranking = font.render("RECORDE", True, (0, 0, 0))
        getRanking = tela.blit(ranking, (LARGURA / 2 - ranking.get_width() / 2, 280))
        sound = font.render("ATIVAR/DESATIVAR SOM", True, (0, 0, 0))
        getSound = tela.blit(sound, (LARGURA / 2 - sound.get_width() / 2, 350))
        sair = font.render("SAIR", True, (0, 0, 0))
        getExit = tela.blit(sair, (LARGURA / 2 - sair.get_width() / 2, 420))
        if getStart.collidepoint((mx, my)):
            if click:
                game()
        if getOptions.collidepoint((mx, my)):
            if click:
                options()
        if getRanking.collidepoint((mx, my)):
            if click:
                rank()
        if getExit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                exit()
        if getSound.collidepoint((mx, my)):
            if click:
                if soundActive == True:
                    soundActive = False
                    som_fundo.stop()
                else:
                    soundActive = True
                    som_fundo.play(-1)
                click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def game():
    global pontos, clock, soundActive, som_mask, som_colisao, recorde
    colidiu = False
    while True:
        relogio.tick(clock)
        tela.fill(BRANCO)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and colidiu == False:
                    if personagem.rect.y != personagem.pos_y_inicial:
                        pass
                    else:
                        personagem.pular()
                if event.key == K_r and colidiu == True:
                    reiniciarJogo()
                    game()
                if event.key == K_b and colidiu == True:
                    reiniciarJogo()
                    main_menu()
        colisoes = pygame.sprite.spritecollide(personagem, grupo_obstaculos, False, pygame.sprite.collide_mask)
        getMask = pygame.sprite.spritecollide(personagem, mascaras, False, pygame.sprite.collide_mask)

        tela.blit(fundo, (0, 0))

        todas_as_sprites.draw(tela)

        if getMask:
            pontos += 1
            if soundActive == True:
                som_mask.play()
            global escolha_obstaculo
            escolha_obstaculo = choice([0, 2, 3])
            virus.rect.x = LARGURA
            mask.rect.x = LARGURA
            virus.escolha = escolha_obstaculo
            mask.escolha = escolha_obstaculo

        if virus.rect.topright[0] <= 0 or mask.rect.topright[0] <= 0:
            if(escolha_obstaculo == 1):
                escolha_obstaculo = choice([0, 2, 3])
            else:
                escolha_obstaculo = choice([0, 1, 2, 3])
            virus.rect.x = LARGURA
            mask.rect.x = LARGURA
            virus.escolha = escolha_obstaculo
            mask.escolha = escolha_obstaculo

        if colisoes and colidiu == False:
            if soundActive == True:
                som_colisao.play()
            colidiu = True
        if colidiu == True:
            gameOver = font.render("GAME OVER", True, (0, 0, 0))
            tela.blit(gameOver, (LARGURA / 2 - gameOver.get_width() / 2, ALTURA / 2 - gameOver.get_height() / 2))
            info = fontInstruction.render("Pressione R para reiniciar ou B para voltar", True, (0, 0, 0))
            tela.blit(info, (LARGURA / 2 - info.get_width() / 2, (ALTURA / 2 - info.get_height() / 2) + 40))
            if pontos > recorde:
                recorde = pontos
            #pass
        else:
            todas_as_sprites.update()

        score_text = fontInstruction.render('Score: ' + str(pontos), True, (0, 0, 0))
        tela.blit(score_text, (525, 25))
        clock += 0.006
        pygame.display.flip()

def options():
    click = False
    while True:
        tela.fill((0, 0, 0))
        tela.blit(fundo, (0, 0))
        instructions = font.render("INSTRUÇÕES", True, (0, 0, 0))
        tela.blit(instructions, (LARGURA/2 - instructions.get_width()/2, 40))
        instructions1 = fontInstruction.render("Supere os obstáculos", True, (0, 0, 0))
        tela.blit(instructions1, (LARGURA / 2 - instructions1.get_width() / 2, 140))
        instructions2 = fontInstruction.render("Para pular pressione espaço", True, (0, 0, 0))
        tela.blit(instructions2, (LARGURA / 2 - instructions2.get_width() / 2, 200))
        instructions3 = fontInstruction.render("A pontuação é definida pela quantidade de máscaras", True, (0, 0, 0))
        tela.blit(instructions3, (LARGURA / 2 - instructions3.get_width() / 2, 260))
        instructions4 = fontInstruction.render("A velocidade aumenta ao longo do jogo", True, (0, 0, 0))
        tela.blit(instructions4, (LARGURA / 2 - instructions4.get_width() / 2, 320))
        back = anotherFont.render("VOLTAR", True, (0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        getBack = tela.blit(back, (475, 425))
        if getBack.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def rank():
    global recorde
    click = False
    while True:
        tela.fill((0, 0, 0))
        tela.blit(fundo, (0, 0))
        pontuacao = font.render("PONTUAÇÃO MÁXIMA", True, (0, 0, 0))
        tela.blit(pontuacao, (LARGURA / 2 - pontuacao.get_width() / 2, 40))
        getScore = fontInstruction.render("Recorde atual: " + str(recorde), True, (0, 0, 0))
        tela.blit(getScore, (LARGURA / 2 - getScore.get_width() / 2, ALTURA / 2 - getScore.get_height() / 2))
        back = anotherFont.render("VOLTAR", True, (0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        getBack = tela.blit(back, (475, 425))
        if getBack.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def reiniciarJogo():
    global pontos, clock, colidiu, escolha_obstaculo
    pontos = 0
    clock = 40
    colidiu = False
    personagem.rect.y = ALTURA - 64 - 96
    personagem.pulo = False
    mask.rect.x = LARGURA
    virus.rect.x = LARGURA
    escolha_obstaculo = choice([0, 1, 2, 3])


main_menu()