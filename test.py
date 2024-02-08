import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
CLOCK = pygame.time.Clock()
running = True
DT = 0
VEL = 1100
FPS = 144


# will be changed to a pixel art background
SCREEN.fill("black")


class Bullet:
    pass


class Enemy:
    pass

    def draw_enemies():
        pass


class Friendly_Spaceship:
    def __init__(self):
        self.player_pos = pygame.Vector2(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 200)
        self.imp = pygame.image.load(
            "./dd4af67c-c3f1-434e-9dad-659ef705893e.png"
        ).convert()
        self.imp = pygame.transform.scale(self.imp, (200, 200))

    def handle_movement(self, keys, player_pos):
        if keys[pygame.K_w] and player_pos.y > (SCREEN_HEIGHT * 2 / 3):
            player_pos.y -= VEL * DT
        if keys[pygame.K_s] and player_pos.y < (SCREEN_HEIGHT - 200):
            player_pos.y += VEL * DT
        if keys[pygame.K_a] and player_pos.x > 0:
            player_pos.x -= VEL * DT
        if keys[pygame.K_d] and player_pos.x < (SCREEN_WIDTH - 200):
            player_pos.x += VEL * DT

    def draw_friendly_spaceship(self, imp, player_pos):
        SCREEN.blit(imp, (player_pos, imp.get_size()))


friendly_spaceship = Friendly_Spaceship()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # DT is delta time in seconds since last frame, used for framerate independent physics.

    keys = pygame.key.get_pressed()
    friendly_spaceship.handle_movement(keys, friendly_spaceship.player_pos)

    friendly_spaceship.draw_friendly_spaceship(
        friendly_spaceship.imp, friendly_spaceship.player_pos
    )
    pygame.display.update()

    DT = CLOCK.tick(144) / 1000

pygame.quit()
