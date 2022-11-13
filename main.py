import pygame

pygame.init()

#CRIAR JANELA
window = pygame.display.set_mode([1280, 700]) # -> DEFINIR TAMANHO DA JANELA
title = pygame.display.set_caption('Futball Pong') # -> DEFINIFR NOME DA APLICAÇÃO

winner = pygame.image.load('assets/win.png')

score1 = 0
score1Imagem = pygame.image.load('assets/score/0.png')
score2 = 0
score2Imagem = pygame.image.load('assets/score/0.png')

# CARREGAR IMAGENS
field = pygame.image.load('assets/field.png')

player1 = pygame.image.load('images/jogador1.png')
player1Y= 230
player1MoveUp = False
player1MoveDown = False

player2 = pygame.image.load('images/jogador2.png')
player2Y= 230

ball = pygame.image.load('images/bola.png')
ballX = 615
ballY= 340
ballDirection = -4
ballDirectionY = 2

#DEFINIR POSIÇÃO DE IMAGENS NA TELA
def elementosDesenho():
    if score1 or score2 < 5:
        window.blit(field, (0, 0))  # É IMPORTANTE DEFIFNIR UMA IMAGEM DE FUNDO COM TAMANHO EQUIVALENTE DA JANELA
        window.blit(player1, (100, player1Y))
        window.blit(player2, (1100, player2Y))
        window.blit(ball, (ballX, ballY))
        window.blit(score1Imagem, (515, 50))
        window.blit(score2Imagem, (695, 50))
        moverBola()
        moverJogador()
        moverJogador2()
    else:
        window.blit(winner, (300, 330))

def moverJogador():
    global player1Y

    if player1MoveUp:
        player1Y -= 5
    else: player1Y += 0

    if player1MoveDown:
        player1Y += 5
    else: player1Y -= 0

    if player1Y <= 0:
        player1Y = 0
    elif player1Y >= 600:
        player1Y = 600

def moverJogador2():
    global player2Y
    player2Y = ballY


def moverBola():
    global ballX
    global ballY
    global ballDirection
    global ballDirectionY
    global score1
    global score1Imagem
    global score2
    global score2Imagem

    ballX += ballDirection
    ballY += ballDirectionY

    if ballX < 200:
        if player1Y < ballY + 25:
            if player1Y + 80 > ballY:
                ballDirection *= -1

    if ballX > 1050:
        if player2Y < ballY + 25:
            if player2Y + 80 > ballY:
                ballDirection *= -1

    if ballY > 620:
        ballDirectionY *= -1
    elif ballY <= 0:
        ballDirectionY *= -1

    if ballX < -50:
        ballX = 615
        ballY = 340
        ballDirectionY *= -1
        ballDirection *= 1
        score2 += 1
        score2Imagem = pygame.image.load(f'assets/score/{str(score2)}.png')
    elif ballX > 1290:
        ballX = 615
        ballY = 340
        ballDirectionY *= -1
        ballDirection *= 1
        score1 += 1
        score1Imagem = pygame.image.load(f'assets/score/{str(score1)}.png')

# CRIAR UM LOOP PARA PODER MANTER A JANELA ATIVA E TAMBEM PARA PODER FECHAR
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT: # -> EVENTO DE FECHAR A JANELA
            loop = False

        if events.type == pygame.KEYDOWN: # TIPO DE TECLA PRESSIONADA
            if events.key == pygame.K_w: # -> SERVE PARA FAZER O MOVIMENTO DO JOGADOR
                player1MoveUp = True
            if events.key == pygame.K_s:
                player1MoveDown = True
        if events.type == pygame.KEYUP: # TIPO DE TECLA PRESSIONADA
            if events.key == pygame.K_w: # -> SERVE PARA FAZER O MOVIMENTO DO JOGADOR
                player1MoveUp = False
            if events.key == pygame.K_s:
                player1MoveDown = False

    elementosDesenho()

    pygame.display.update()