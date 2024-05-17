import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, VEL, dt


class Player:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_pos = pygame.Vector2(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 150)
        self.player_size = (150, 150)
        self.player_image = pygame.image.load("./assets/images/Statek.png").convert()
        self.player_image = pygame.transform.scale(self.player_image, self.player_size)

    def draw_player(self, screen):
        screen.blit(
            self.player_image,
            (self.player_pos, self.player_size),
        )
