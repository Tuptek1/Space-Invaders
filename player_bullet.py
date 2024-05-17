import pygame
from constants import BLUE


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = -7
        self.bullets_list = []

    def handle_bullet(self, bullets):
        for bullet in bullets:
            bullet.y += self.velocity
            if bullet.y < 0:
                bullets.remove(bullet)

    def draw_bullet(self, screen, bullets):
        for bullet in bullets:
            pygame.draw.rect(screen, BLUE, bullet)
