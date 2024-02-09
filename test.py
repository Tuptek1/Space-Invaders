import pygame

# pygame setup
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

BLACK = (0, 0, 0)
VEL = 5
FPS = 144


# will be changed to a pixel art background
SPACE = pygame.transform.scale(
    pygame.image.load("black_background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
)


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

    def handle_movement(self, keys):
        print(self.player_pos.x)
        print(self.player_pos.y)
        if keys[pygame.K_w] and self.player_pos.y > (SCREEN_HEIGHT * 2 / 3):
            self.player_pos.y -= VEL
        if keys[pygame.K_s] and self.player_pos.y < (SCREEN_HEIGHT - 200):
            self.player_pos.y += VEL
        if keys[pygame.K_a] and self.player_pos.x > 0:
            self.player_pos.x -= VEL
        if keys[pygame.K_d] and self.player_pos.x < (SCREEN_WIDTH - 200):
            self.player_pos.x += VEL

    def draw_friendly_spaceship(self):
        SCREEN.blit(SPACE, (0, 0))
        SCREEN.blit(self.imp, (self.player_pos.x, self.player_pos.y))
        pygame.display.update()


# friendly_spaceship = Friendly_Spaceship()
# running = True
# while running:
#     DT = CLOCK.tick(144) / 1000
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # DT is delta time in seconds since last frame, used for framerate independent physics.

#     keys = pygame.key.get_pressed()
#     friendly_spaceship.handle_movement(keys, friendly_spaceship.player_pos)

#     friendly_spaceship.draw_friendly_spaceship(
#         friendly_spaceship.imp, friendly_spaceship.player_pos
#     )


friendly_spaceship = Friendly_Spaceship()


def main():
    CLOCK = pygame.time.Clock()
    running = True

    while running:
        CLOCK.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        friendly_spaceship.handle_movement(keys)

        friendly_spaceship.draw_friendly_spaceship()

    pygame.quit()


if __name__ == "__main__":
    main()
