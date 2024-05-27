import pygame
import random
from constants import RED, SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_IMAGE_PATHS, BLACK, WHITE


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.enemy_image = pygame.image.load(random.choice(ENEMY_IMAGE_PATHS)).convert()
        self.enemy_size = (95, 95)
        self.enemy_image = pygame.transform.scale(self.enemy_image, self.enemy_size)
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

    def draw_enemy(self, screen, enemies_list):
        for enemy in enemies_list:
            x_cord = enemy[0]
            y_cord = enemy[1]
            pygame.draw.rect(screen, WHITE, rect=enemy)
            screen.blit(self.enemy_image, (x_cord, y_cord))
