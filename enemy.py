import pygame
import random
from constants import RED, SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_IMAGE_PATHS


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.enemy_image = pygame.image.load(random.choice(ENEMY_IMAGE_PATHS)).convert()
        self.enemy_size = (75, 75)
        self.enemy_image = pygame.transform.scale(self.enemy_image, self.enemy_size)
        self.rect = self.enemy_image.get_rect()
        self.speed = 2
        self.enemies_list = []
        self.enemy_pos = (40, -100)
        self.row_number = 1

    def spawn_enemy(self, enemies_list):
        enemies_list.append(self.enemy_pos)
        self.enemy_pos = (self.enemy_pos[0] + 100, self.enemy_pos[1])
        # self.enemy_pos = (random.randrange(40, 1140, 100), self.enemy_pos[1])
        # print(self.enemies_list)

    def spawn_enemy_row(self, enemies_list):

        self.enemy_pos = (40, self.enemy_pos[1] + 100)
        for _ in range(12):
            self.spawn_enemy(enemies_list)

    def draw_enemy(self, screen, enemies_list):
        for position in enemies_list:
            screen.blit(self.enemy_image, position)
