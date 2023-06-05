

  <h1 align="center">🎮 Ping Pong Pygames 🎮</h1>



### Este é um projeto simples do famoso jogo Pong implementado em Python usando a biblioteca Pygame.

![Fig.gif](/Pong.gif)


# Requisitos

### - Python 3.x 🐍
### - Pygame 🎮

# Instalação dos Pacotes pyInstaller 🔧

```bash
pyinstaller --onefile ping-pong.py
```

# Executando o jogo ▶️

```bash
python main.py
```

# Set das variáveis 🏗️ 

```python
import pygame
from pygame import mixer
import sys

#Inicializa o Pygame e o mixer, que é responsável pelo processamento de áudio.

pygame.init()
mixer.init()

#Define as dimensões da tela, da raquete e da bola.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 10
PADDLE_SPEED = 10
BALL_SPEED = 3
START = 0
WINNER_SCORE = 5


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

score_b = 0
score_a = 0

font_file = 'Press_Start_2P/PressStart2P-Regular.ttf'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PingPong")

# pygame.rect(x,y,width,height)
paddle_a = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(SCREEN_WIDTH - 20 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                       PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

```

# Renderização do Menu


```python
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Renderização do menu principal
        screen.fill(BLACK)
        title_font = pygame.font.Font(font_file, 36)
        title_text = title_font.render("PingPong", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

        screen.blit(title_text, title_rect)

        title_font = pygame.font.Font(font_file, 16)
        current_time = pygame.time.get_ticks()

        if current_time % 2000 < 1000:
            title_text1 = title_font.render("Pressione espaço para iniciar", True, WHITE)
            title_rect1 = title_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 60))
            screen.blit(title_text1, title_rect1)

        pygame.display.flip()
```

#### A estrutura a seguir é utilizada por desenvolvedores de jogos com a biblioteca Pygame.

Trata-se de uma estrutura comumente utilizada por desenvolvedores de jogos com a biblioteca Pygame.

Essa estrutura envolve a criação de um loop principal (while True) que continua executando indefinidamente até que uma condição de término seja encontrada. Dentro desse loop principal, os eventos são verificados em um loop for para capturar as interações do jogador, como o fechamento da janela ou a pressionar de teclas específicas.

```python
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                    game_loop()
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
```

O bloco funciona da seguinte forma:

```python
current_time = pygame.time.get_ticks()
```
A função é chamada para obter o tempo em milissegundos desde que o jogo começou.

```python
title_font = pygame.font.Font(font_file, 16)
        current_time = pygame.time.get_ticks()
```
O trecho de código verifica se o resto da divisão da variável current_time por 2000 é menor que 1000. Se essa condição for verdadeira, significa que current_time está dentro do intervalo de 0 a 999 milissegundos após cada múltiplo de 2000 milissegundos. Essa verificação é utilizada para criar um efeito de piscar.

Por exemplo, se current_time for 2500, o resto da divisão por 2000 é 500. Como 500 é menor que 1000, a condição é verdadeira e o código dentro do bloco if será executado. Isso resultará na renderização do texto desejado. Esse efeito de piscar é criado porque o texto só será mostrado durante a primeira metade do intervalo de 2000 milissegundos.


## Game 🎮

##### A classe Game representa o estado geral do jogo. Ela contém a lógica principal do jogo, incluindo o loop do jogo, a detecção de colisões, o controle de pontuação e a manipulação de eventos.

# Som 🔊
##### O jogo inclui música de fundo e efeitos sonoros para a colisão da bola com as raquetes e para quando um jogador marca um ponto.

# Controles do Jogo 🕹️ 
##### Os controles do jogo são os seguintes:

| Jogador 1 | Jogador 2 |
| --- | --- |
| W: Mover para cima | Seta para cima: Mover para cima |
| S: Mover para baixo | Seta para baixo: Mover para baixo |
| A: Mover para a esquerda | Seta para a esquerda: Mover para a esquerda |
| D: Mover para a direita | Seta para a direita: Mover para a direita |

# Vamos ver o código do Game 🎮

```python

    def game_loop():
    global ball_dx, ball_dy, score_a, score_b, START, BALL_SPEED # Define as variáveis globais

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # Preenche a tela com a cor preta
       screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 5)
        for i in range(0, SCREEN_HEIGHT, 20):
            pygame.draw.line(screen, BLACK, (0, i), (SCREEN_WIDTH, i), 10)
        pygame.draw.rect(screen, WHITE, paddle_a)
        pygame.draw.rect(screen, WHITE, paddle_b)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Obtém o estado das teclas pressionadas
        keys = pygame.key.get_pressed()

        #Movimento Vertical Raquete A
        if keys[pygame.K_w] and paddle_a.top > 0:
            paddle_a.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_a.bottom < SCREEN_HEIGHT:
            paddle_a.y += PADDLE_SPEED

        #Movimento Vertical Raquete B
        if keys[pygame.K_UP] and paddle_b.top > 0:
            paddle_b.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_b.bottom < SCREEN_HEIGHT:
            paddle_b.y += PADDLE_SPEED

        #Movimento Horizontal Raquete A
        if keys[pygame.K_a] and paddle_a.left > 0:
            paddle_a.x -= PADDLE_SPEED
        if keys[pygame.K_d] and paddle_a.right < SCREEN_WIDTH // 2 - 70:
            paddle_a.x += PADDLE_SPEED

        #Movimento Horizontal Raquete B
        if keys[pygame.K_LEFT] and paddle_b.left > SCREEN_WIDTH // 2 + 70:
            paddle_b.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle_b.right < SCREEN_WIDTH:
            paddle_b.x += PADDLE_SPEED
      
        # Atualização da posição da bola
       
            ball.x += ball_dx
            ball.y += ball_dy

        if ball.colliderect(paddle_a):
            ball.left = paddle_a.right
            ball_dx = -ball_dx
            pygame.mixer.Sound.play(sound_a)

        elif ball.colliderect(paddle_b):
            ball.right = paddle_b.left
            ball_dx = -ball_dx
            pygame.mixer.Sound.play(sound_b)

        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_dy = -ball_dy

        if ball.left <= 0:
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            score_b += 1
            pygame.mixer.Sound.play(hoohoo)
            print(f'Pontos B: {score_b}')

        if ball.right >= SCREEN_WIDTH:
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            score_a += 1
            pygame.mixer.Sound.play(hoohoo)
            print(f'Pontos A: {score_a}')


        #Bola quando bate na extremidade da tela
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_dy = -ball_dy

        #Ponto para o Time B
        if ball.left <= 0:
            score_b += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            point_sound.play()
            # print(score_b)
            if score_b == 5: # Quantidade máxima de pontos para B
                end_game(False)

        #Ponto para o Time A
        elif ball.right >= SCREEN_WIDTH:
            score_a += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            point_sound.play()
            # print(score_a)
            if score_a == 5: # Quantidade máxima de pontos para A
                end_game(True)

        # Placar na Tela
        score_text = font.render(f"{score_a}  {score_b}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        screen.blit(score_text, score_rect)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar FPS
        clock = pygame.time.Clock()
        clock.tick(60)
```

#### Movimento Vertical:

Essa estrutura de código controla o movimento vertical das raquetes A e B, verificando se as teclas W (cima) e S (baixo) estão pressionadas para mover a raquete A, e se as teclas de seta para cima e para baixo estão pressionadas para mover a raquete B. Além disso, são realizadas verificações adicionais para garantir que as raquetes não ultrapassem as bordas superior e inferior da tela, evitando que elas saiam da área de jogo.

```python
        #Movimento Vertical Raquete A

        # Verifica se a tecla W está pressionada e se a raquete A não está no topo da tela 
        if keys[pygame.K_w] and paddle_a.top > 0: 
            paddle_a.y -= PADDLE_SPEED  # Move a raquete A para cima
        if keys[pygame.K_s] and paddle_a.bottom < SCREEN_HEIGHT:
            paddle_a.y += PADDLE_SPEED

        #Movimento Vertical Raquete B

        # Verifica se a tecla de seta para cima está pressionada e se a raquete B não está no topo da tela
        if keys[pygame.K_UP] and paddle_b.top > 0:
            paddle_b.y -= PADDLE_SPEED # Move a raquete B para cima
        if keys[pygame.K_DOWN] and paddle_b.bottom < SCREEN_HEIGHT:
            paddle_b.y += PADDLE_SPEED
```
#### Movimento Horizontal:

Essa estrutura de código controla o movimento horizontal das raquetes A e B, verificando se as teclas A (esquerda) e D (direita) estão pressionadas para mover a raquete A, e se as teclas de seta para a direita e para a esquerda estão pressionadas para mover a raquete B. Além disso, são realizadas verificações adicionais para garantir que as raquetes não ultrapassem as bordas esquerda e direita da tela, evitando que elas saiam da área de jogo.

```python
        #Movimento Horizontal Raquete A

        # Verifica se a tecla A está pressionada e se a raquete A não está no limite esquerdo da tela
        if keys[pygame.K_a] and paddle_a.left > 0:
            paddle_a.x -= PADDLE_SPEED # Move a raquete A para a esquerda
        if keys[pygame.K_d] and paddle_a.right < SCREEN_WIDTH // 2 - 70:
            paddle_a.x += PADDLE_SPEED

        #Movimento Horizontal Raquete B

         # Verifica se a tecla de seta para a esquerda está pressionada e se a raquete B não está no limite esquerdo da tela
        if keys[pygame.K_LEFT] and paddle_b.left > SCREEN_WIDTH // 2 + 70: # Move a raquete B para a esquerda
            paddle_b.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle_b.right < SCREEN_WIDTH:
            paddle_b.x += PADDLE_SPEED
```

####  Sistema de Colisão:

Esse código atualiza a posição da bola e lida com colisões entre a bola e as raquetes A e B, reproduzindo um som quando colidem. Após uma colisão, a posição da bola é ajustada e sua direção horizontal é invertida. 

```python
        # Atualização da posição da bola
        ball.x += ball_dx
        ball.y += ball_dy
        
        # Verifica se houve colisão entre a raquete A e a bola, se sim, emite o som
        if ball.colliderect(paddle_a):
            ball.left = paddle_a.right
            ball_dx = -ball_dx
            collision_sound_A.play()

        # Verifica se houve colisão entre a raquete B e a bola, se sim, emite o som
        elif ball.colliderect(paddle_b):
            ball.right = paddle_b.left
            ball_dx = -ball_dx
            collision_sound_B.play()

        # Verifica se houve colisão entre a raquete A e a bola no topo da raquete, se sim, emite o som
        elif ball.colliderect(paddle_a):
            ball.left = paddle_b.topright
            ball_dx = -ball_dx
            collision_sound_B.play()

        # Verifica se houve colisão entre a raquete B e a bola no topo da raquete, se sim, emite o som
        elif ball.colliderect(paddle_b):
            ball.right = paddle_b.topleft
            ball_dx = -ball_dx
            collision_sound_B.play()
```

#### Pontuação:

Esse código verifica se a bola ultrapassou a extremidade esquerda da tela, indicando um ponto para o Time B. Incrementa o placar do Time B, reposiciona a bola no centro da tela, inverte sua direção horizontal, reproduz um som de ponto e verifica se o Time B alcançou a quantidade máxima de pontos permitida para encerrar o jogo. O mesmo ocorre para o Time A.


```python
        #Bola quando bate na extremidade da tela
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_dy = -ball_dy

        #Verifica se a bola ultrapassou a extremidade esquerda da tela, o que significa um ponto para o Time B.
        if ball.left <= 0:
            score_b += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            point_sound.play()
            # print(score_b)
            if score_b == 10: # Quantidade máxima de pontos para B
                end_game(False)

        #Verifica se a bola ultrapassou a extremidade direita da tela, o que significa um ponto para o Time A.
        elif ball.right >= SCREEN_WIDTH:
            score_a += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            point_sound.play()
            # print(score_a)
            if score_a == 10: # Quantidade máxima de pontos para A
                end_game(True)

        # Placar na Tela
        score_text = font.render(f"{score_a}  {score_b}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        screen.blit(score_text, score_rect)
       
```
# Fim de Jogo

Esse código implementa a tela de fim de jogo, apresentando quem foi o vencedor, permitindo reiniciar ou encerrar o jogo de acordo com as teclas pressionadas.

```python
   def end_game(winner):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
       
        mixer.music.stop()
        screen.fill(BLACK)
        #Comente
        if winner:
            winner_text = "Player 2 Wins!"
        else:
            winner_text = "Player 1 Wins!"

        # Renderização da tela de fim de jogo
       screen.fill(BLACK)
        title_font = pygame.font.Font(font_file, 36)
        title_text = title_font.render("Vencedor", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        title_font1 = pygame.font.Font(font_file, 32)
        title_text1 = title_font1.render(winner, True, WHITE)
        title_rect1 = title_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 40))
        screen.blit(title_text1, title_rect1)
```
# Reiniciando o Jogo

Restaura as váriaveis para seus valores iniciais, permitindo que o jogo seja reiniciado.

```python
  def reset_game():
    global paddle_a, paddle_b, ball, ball_dx, ball_dy, score_a, score_b
```

