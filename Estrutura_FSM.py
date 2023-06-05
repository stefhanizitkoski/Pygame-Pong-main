import pygame
import sys

# (O código de inicialização e variáveis globais permanecem o mesmo)
pygame.init()

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


# SOM

music_game = pygame.mixer.Sound('audios/music_game.mp3')
sound_a = pygame.mixer.Sound('audios/Sound_A.wav')
sound_b = pygame.mixer.Sound('audios/Sound_B.wav')
hoohoo = pygame.mixer.Sound('audios/hoohooo.wav')


# Funções de estado
def main_menu():
    global score_a, score_b

    pygame.mixer.Sound.play(music_game)

    score_b = 0
    score_a = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()

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

def game_loop():
    global ball_dx, ball_dy, score_a, score_b, START, BALL_SPEED

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 5)
        for i in range(0, SCREEN_HEIGHT, 20):
            pygame.draw.line(screen, BLACK, (0, i), (SCREEN_WIDTH, i), 10)
        pygame.draw.rect(screen, WHITE, paddle_a)
        pygame.draw.rect(screen, WHITE, paddle_b)
        pygame.draw.ellipse(screen, WHITE, ball)

        title_font = pygame.font.Font(font_file, 36)
        title_text = title_font.render(f"{score_a}  {score_b}", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(title_text, title_rect)

        title_font_a = pygame.font.Font(font_file, 50)
        title_text_a = title_font_a.render('A', True, WHITE)
        title_rect_a = title_text_a.get_rect(center=(50, SCREEN_HEIGHT - 50))
        screen.blit(title_text_a, title_rect_a)

        title_font_b = pygame.font.Font(font_file, 50)
        title_text_b = title_font_b.render('B', True, WHITE)
        title_rect_b = title_text_b.get_rect(center=(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50))
        screen.blit(title_text_b, title_rect_b)

        title_font_name = pygame.font.Font(font_file, 10)
        title_text_name = title_font_name.render('Stéfhani', True, WHITE)
        title_rect_name = title_text_name.get_rect(center=(SCREEN_WIDTH - 60, SCREEN_HEIGHT - 12))
        screen.blit(title_text_name, title_rect_name)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle_a.top > 0:
            paddle_a.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_a.bottom < SCREEN_HEIGHT:
            paddle_a.y += PADDLE_SPEED
        if keys[pygame.K_a] and paddle_a.left > 20:
            paddle_a.x -= PADDLE_SPEED
        if keys[pygame.K_d] and paddle_a.right < (SCREEN_WIDTH // 2) - 50:
            paddle_a.x += PADDLE_SPEED
        if keys[pygame.K_UP] and paddle_b.top > 0:
            paddle_b.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_b.bottom < SCREEN_HEIGHT:
            paddle_b.y += PADDLE_SPEED
        if keys[pygame.K_LEFT] and paddle_b.left > (SCREEN_WIDTH // 2) + 50:
            paddle_b.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle_b.right < (SCREEN_WIDTH - 20):
            paddle_b.x += PADDLE_SPEED

        if keys[pygame.K_SPACE]:
            START += 1

        if START % 2 == 0:
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

        pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(60)

        if score_a == WINNER_SCORE:
            end_game('Jogador A')
        elif score_b == WINNER_SCORE:
            end_game('Jogador B')


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
        # Desenhe o texto de vitória e instruções aqui

        current_time = pygame.time.get_ticks()
        if current_time % 2000 < 1000:
            title_font_main_menu = pygame.font.Font(font_file, 10)
            title_text_main_menu = title_font_main_menu.render("Pressione espaço para iniciar", True, WHITE)
            title_rect_main_menu = title_text_main_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
            screen.blit(title_text_main_menu, title_rect_main_menu)

        pygame.display.flip()


def reset_game():
    global paddle_a, paddle_b, ball, ball_dx, ball_dy, score_a, score_b


main_menu()