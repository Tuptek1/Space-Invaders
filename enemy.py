import pygame
import random 

RED = (255, 0, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__ (self, x,y): 
        super().__init__()
        self.image == pygame.image.load("./assets/images/enemy.png").convert() 
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topLeft = (x,y)
        self.speed = 2

    def update(self, screenWidth):
        self.rect.x += self.speed
        if self.rect.right > screenWidth or self.rect.left <= 0:
            self.rect.y += 40 # Move down 
            self.speed = -self.speed

enemies = pygame.sprite.Group()

def spawn_enemy(screenWidth, screenHeight): 
    x = random.rand(0, screenWidth - 50)
    y = random.rand(0, screenHeight - 50)
    enemy = Enemy(x,y)
    enemies.add(enemy)