import pygame

WHITE = (255, 255, 255)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.bullet_pos = self.image.get_rect()
        self.speed = -1
        self.bullets_list = []

    def create_bullet(self, bullets, player_pos):
        self.bullet_pos.x = player_pos.x + 100
        self.bullet_pos.y = player_pos.y
        bullet = self.image
        bullets.append(bullet)

    def draw_bullet(self, screen, bullet):
        if self.bullet_pos.y > 0:
            self.bullet_pos.y += self.speed
        screen.blit(bullet, self.bullet_pos)
        print(self.bullet_pos)
