import pygame
from bullet import Bullet

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

VEL = 1100
BORDER = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_WIDTH)

player_pos = pygame.Vector2(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 200)

bullet = Bullet()
bullets = bullet.bullets_list


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    imp = pygame.image.load("./assets/images/spaceship.png").convert()
    imp = pygame.transform.scale(imp, (200, 200))

    screen.blit(imp, (player_pos, imp.get_size()))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > (SCREEN_HEIGHT * 2 / 3):
        player_pos.y -= VEL * dt
    if keys[pygame.K_s] and player_pos.y < (SCREEN_HEIGHT - 200):
        player_pos.y += VEL * dt
    if keys[pygame.K_a] and player_pos.x > 0:
        player_pos.x -= VEL * dt
    if keys[pygame.K_d] and player_pos.x < (SCREEN_WIDTH - 200):
        player_pos.x += VEL * dt
    if keys[pygame.K_SPACE]:
        bullet.create_bullet(bullets, player_pos)

    for bullet_instance in bullets:
        bullet.draw_bullet(screen, bullet_instance)

    pygame.display.update()
    delta_time = clock.tick(144) / 1000

pygame.quit()
