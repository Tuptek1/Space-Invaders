import pygame
import random
from constants import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.enemy_size = (85, 85)
        self.speed = 2
        self.enemy_pos_list = []
        # [((enemypos), enemy_rect, enemy_image)]

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
            x_cord = enemy_pos[0]
            y_cord = enemy_pos[1]

            pygame.draw.rect(screen, WHITE, rect=enemy[1])
            screen.blit(enemy[2], (x_cord, y_cord))

    def enemy_shoot(self, enemy_pos_list, enemy_bullets_list):
        for i in enemy_pos_list:
            shoot = random.choice([True, False])

            if shoot:
                enemy_pos = i[0]
                enemy_bullet = pygame.Rect(
                    (enemy_pos[0] + (self.enemy_size[0] // 2)),
                    (enemy_pos[1] + self.enemy_size[1]),
                    5,
                    20,
                )
                enemy_bullets_list.append(enemy_bullet)
