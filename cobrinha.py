import pygame
import time
import random

# Initialize pygame
pygame.init()

# Custom colors
background_color = (0, 0, 0)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)
font_color = (255, 255, 255)

# Screen dimensions
screen_width = 600
screen_height = 450

# Screen configuration
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game by Kin')

# Clock to control the update rate
clock = pygame.time.Clock()

# Game settings
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 25)


def render_score(score):
    value = score_font.render("Placar: " + str(score), True, font_color)
    screen.blit(value, [10, 10])


def render_timer(timer):
    timer_display = score_font.render("Tempo de execução: {:.1f}".format(timer), True, font_color)
    screen.blit(timer_display, [10, screen_height - 30])


def render_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, snake_color, [segment[0], segment[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    start_time = time.time()
    last_food_time = pygame.time.get_ticks()

    while not game_over:

        while game_close == True:
            screen.fill(background_color)
            message("Perdeu! A tecla C continua e Q finaliza", font_color)
            render_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width:
            x1 = 0
        elif x1 < 0:
            x1 = screen_width - snake_block

        if y1 >= screen_height:
            y1 = 0
        elif y1 < 0:
            y1 = screen_height - snake_block

        x1 += x1_change
        y1 += y1_change

        screen.fill(background_color)

        current_time = pygame.time.get_ticks()
        if current_time - last_food_time >= 5000:  # 5000 milliseconds = 5 seconds
            last_food_time = current_time
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

        pygame.draw.rect(screen, food_color, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        render_snake(snake_list)
        render_score(length_of_snake - 1)

        current_time = time.time()
        elapsed_time = current_time - start_time
        render_timer(elapsed_time)

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
