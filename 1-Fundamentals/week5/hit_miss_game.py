import pygame
import sys
import random

pygame.init()  # initializing pygame
WIDTH = 600
HEIGHT = 400

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)

player_dim = 50  # variable to hold player dimensions
# list variable to hold player position
player_pos = [WIDTH/2, HEIGHT - 3 * player_dim]

enemy_size = 50  # initializing enemy position
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

SPEED = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

end_game = False
clock = pygame.time.Clock()  # to set frame rate

while not end_game:  # intorduce a while loop that will ran when game is not over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:  # from pygame library
            x = player_pos[0]  # position co-ordinates for player
            y = player_pos[1]

            if event.key == pygame.K_LEFT:  # left move on keydown
                x -= player_dim
            elif event.key == pygame.K_RIGHT:  # right move on keydown
                x += player_dim

            player_pos = [x, y]  # new player position

        screen.fill(BACKGROUND_COLOR)  # fill screen with black background
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED  # make enemy block move downwards
        else:
            enemy_pos[0] = random.randint(0, WIDTH-enemy_size)
            enemy_pos[1] = 0

    # draw palyer rectangle
    pygame.draw.rect(
        screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(
        screen, RED, (player_pos[0], player_pos[1], player_dim, player_dim))
    clock.tick(30)

    pygame.display.update()
