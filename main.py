import pygame
from bullet import Bullet

WHITE = (255, 255, 255)
RED = (255, 87, 51)
# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    clock = pygame.time.Clock()
    running = True
    dt = 0

    VEL = 1100
    BORDER = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_WIDTH)

    player_pos = pygame.Vector2(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 150)

    player_size = (150, 150)
    imp = pygame.image.load("./assets/images/Statek.png").convert()
    imp = pygame.transform.scale(imp, player_size)

    bg = pygame.image.load("./assets/images/Map.png").convert()

    bullet_class = Bullet()
    bullets_list = bullet_class.bullets_list

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(player_pos.y, player_pos.x // 2)
                    bullet = pygame.Rect(
                        (player_pos.x - 2.5) + (player_size[0] // 2),
                        player_pos.y,
                        5,
                        20,
                    )
                    bullets_list.append(bullet)

        screen.blit(bg, (0, 0))
        screen.blit(imp, (player_pos, imp.get_size()))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_pos.y > (SCREEN_HEIGHT * 2 / 3):
            player_pos.y -= VEL * dt
        if keys[pygame.K_s] and player_pos.y < (SCREEN_HEIGHT - player_size[0]):
            player_pos.y += VEL * dt
        if keys[pygame.K_a] and player_pos.x > 0:
            player_pos.x -= VEL * dt
        if keys[pygame.K_d] and player_pos.x < (SCREEN_WIDTH - player_size[0]):
            player_pos.x += VEL * dt

        bullet_class.handle_bullet(bullets_list)
        bullet_class.draw_bullet(screen, bullets_list)

        pygame.display.update()
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(144) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
