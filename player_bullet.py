import pygame
from constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 3.5

    def handle_player_bullet(self, bullets):
        for bullet in bullets:
            bullet.y += -self.velocity
            if bullet.y < 0:
                bullets.remove(bullet)

    def handle_enemy_bullet(self, bullets):
        for bullet in bullets:
            bullet.y -= -self.velocity
            if bullet.y > SCREEN_HEIGHT:
                bullets.remove(bullet)

    def draw_bullet(self, screen, player_bullets, enemy_bullets):
        for enemy_bullet in enemy_bullets:
            pygame.draw.rect(screen, RED, enemy_bullet)
        for player_bullet in player_bullets:
            pygame.draw.rect(screen, BLUE, player_bullet)
