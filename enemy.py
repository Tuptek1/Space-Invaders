import pygame
import random
from constants import RED, SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_IMAGE_PATHS, BLACK, WHITE


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.enemy_size = (85, 85)
        self.speed = 2
        self.enemy_pos_list = []
        self.enemy_pos = (40, -100)
        self.row_number = 1
        self.enemy_rect = pygame.Rect(0, 0, 0, 0)

    def move_enemy_x(self):
        self.enemy_pos = (
            self.enemy_pos[0] + 100,
            self.enemy_pos[1],
        )

    def move_enemy_y(self):
        self.enemy_pos = (
            self.enemy_pos[0],
            self.enemy_pos[1] + 100,
        )

    def draw_enemies(self, enemy_pos_list, screen):
        for enemy in enemy_pos_list:
            enemy_pos = enemy[0]

            # print(enemy)
            x_cord = enemy_pos[0]
            y_cord = enemy_pos[1]
            # print(image, enemy, x_cord, y_cord)
            pygame.draw.rect(screen, WHITE, rect=enemy[1])
            screen.blit(enemy[2], (x_cord, y_cord))
