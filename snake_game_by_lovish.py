import pygame
import random
import time
pygame.init()

pygame.mixer.init()

# mainsound = pygame.mixer.sound('background.mp3')

#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (77, 202, 240)

screen_width = 600
screen_height = 500
flag = 0
depth = 0
game_window = pygame.display.set_mode((screen_width, screen_height), flag, depth)

#background image
bgimg = pygame.image.load("front.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

inimg = pygame.image.load("inner.jpg")
inimg = pygame.transform.scale(inimg, (screen_width, screen_height)).convert_alpha()

overimg = pygame.image.load("Game_over.webp")
overimg = pygame.transform.scale(overimg, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 45)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(game_window, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
    pygame.mixer.music.load("starting_final.mp3")
    pygame.mixer.music.play(loops=-1)

    exit_game = False
    while not exit_game:
        game_window.fill(white)
        game_window.blit(bgimg, (0,0))
        # text_screen("Welcome to Snake Game...", black, 100, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play()
                    #own logic
                    # mainsound.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)

#game_loop
def gameloop():
    # pygame.mixer.music.load("background.mp3")
    # pygame.mixer.music.play()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55

    food_x = random.randint(20, screen_height / 2)
    food_y = random.randint(20, screen_width / 2)

    score = 0

    velocity_x = 0
    velocity_y = 0
    init_velocity = 3
    snake_size = 15
    fps = 40
    snk_list = []
    snk_length = 1

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            # pygame.mixer.music.load("gameover.mp3")
            # pygame.mixer.music.play()
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill(white)
            game_window.blit(overimg, (0, 0))
            # text_screen("Game Over! Press Enter To Cont..", red, 45, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # if event.key == pygame.K_f:
                    #     init_velocity += 4
                    #
                    # if event.key == pygame.K_s:
                    #     init_velocity -= 4

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                pygame.mixer.music.load("eating.wav")
                pygame.mixer.music.play()
                score+=1
                pygame.mixer.music.load("eating.wav")
                pygame.mixer.music.play()
                time.sleep(0.06)
                pygame.mixer.music.load("background.mp3")
                pygame.mixer.music.play()
                # print("Score: ", score)
                food_x = random.randint(20, screen_height / 2)
                food_y = random.randint(20, screen_width / 2)
                snk_length += 5
                if score > int(highscore):
                    highscore = score

            game_window.fill(white)
            game_window.blit(inimg, (0, 0))
            text_screen("Score: " + str(score) + "    highscore : " + str(highscore), white , 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_window.fill(white)
                game_over = True
                # pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.stop()
                pygame.mixer.music.load("gameov_final.wav")
                pygame.mixer.music.play()
                # time.sleep(0.2)

                # game_window.blit(overimg, (0, 0))

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                # pygame.mixer.music.load("game over.wav")
                pygame.mixer.music.stop()
                pygame.mixer.music.load("gameov_final.wav")
                pygame.mixer.music.play()
                # game_window.fill(white)
                game_window.blit(overimg, (0, 0))
                # print("game over")
            # pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(game_window, yellow, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
# gameloop()