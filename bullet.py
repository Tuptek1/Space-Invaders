import pygame
import time

WHITE = (255, 255, 255)
RED = (255, 87, 51)
BLUE = (51, 131, 255)


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
            # print(bullet)

    def draw_bullet(self, screen, bullets):
        for bullet in bullets:
            pygame.draw.rect(screen, BLUE, bullet)
