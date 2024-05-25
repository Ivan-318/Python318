import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
cell_size = 20
game_speed = 15

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Змейка')


def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))


def create_food():
    food_x = random.randint(0, screen_width - cell_size)
    food_y = random.randint(0, screen_height - cell_size)
    return food_x, food_y


def game():
    snake_list = [[screen_width // 2, screen_height // 2]]
    snake_length = 1
    direction = 'RIGHT'
    food_x, food_y = create_food()
    score = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        if direction == 'UP':
            snake_list[0][1] -= cell_size
        elif direction == 'DOWN':
            snake_list[0][1] += cell_size
        elif direction == 'LEFT':
            snake_list[0][0] -= cell_size
        elif direction == 'RIGHT':
            snake_list[0][0] += cell_size

        if snake_list[0][0] == food_x and snake_list[0][1] == food_y:
            food_x, food_y = create_food()
            score += 10
            snake_length += 1

        new_segment = list(snake_list[-1])
        snake_list.append(new_segment)

        for i in range(len(snake_list) - 1, 0, -1):
            snake_list[i] = list(snake_list[i - 1])

        pygame.draw.rect(screen, red, (food_x, food_y, cell_size, cell_size))

        draw_snake(snake_list)

        pygame.display.update()

        if snake_list[0][0] < 0 or snake_list[0][0] >= screen_width or snake_list[0][1] < 0 or snake_list[0][
            1] >= screen_height:
            pygame.quit()
            sys.exit()

        if snake_list[0] in snake_list[1:]:
            pygame.quit()
            sys.exit()

        clock.tick(game_speed)


game()
