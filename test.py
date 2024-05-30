import pygame
import random
from constants import ENEMY_IMAGE_PATHS

pygame.init()

WHITE = (255, 255, 255)

BACKGROUND_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

enemy_image_list = ENEMY_IMAGE_PATHS
enemy_pos_list = [
    ((120, 120), enemy_image_list[0]),
    ((220, 220), enemy_image_list[1]),
    ((320, 320), enemy_image_list[2]),
]


def draw_enemies(enemy_pos_list):
    # print(enemy_image_list)
    for enemy in enemy_pos_list:

        enemy_pos = enemy[0]

        x_cord = enemy_pos[0]
        y_cord = enemy_pos[1]
        # print(image, enemy, x_cord, y_cord)
        pygame.draw.rect(screen, WHITE, rect=enemy[1])
        screen.blit(enemy[2], (x_cord, y_cord))
        print(enemy_pos_list)


WIDTH, HEIGHT = (1000, 1000)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceGenerationTest")

display_stars = False
running = True  #
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                display_stars = True

    screen.fill(BACKGROUND_COLOR)

    if display_stars:
        draw_enemies(enemy_pos_list)

    pygame.display.update()
