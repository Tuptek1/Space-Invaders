import pygame
from player_bullet import Bullet
from enemy import Enemy
from player import Player
from constants import (
    WHITE,
    RED,
    BLACK,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    VEL,
    dt,
    SCORE_POS,
    GREEN,
)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
font = pygame.font.Font("freesansbold.ttf", 32)

player_class = Player()
bullet_class = Bullet()
enemy_class = Enemy()


def main():
    SCORE = 0

    clock = pygame.time.Clock()
    running = True
    display_enemies = False

    BORDER = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_WIDTH)
    background_image = pygame.image.load("./assets/images/Map.png").convert()
    bullets_list = bullet_class.bullets_list
    enemies_list = enemy_class.enemies_list
    row_counter = 1

    while running:

        def player_movement():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and player_class.player_pos.y > (SCREEN_HEIGHT * 2 / 3):
                player_class.player_pos.y -= VEL * dt
            if keys[pygame.K_s] and player_class.player_pos.y < (
                SCREEN_HEIGHT - player_class.player_size[0]
            ):
                player_class.player_pos.y += VEL * dt
            if keys[pygame.K_a] and player_class.player_pos.x > 0:
                player_class.player_pos.x -= VEL * dt
            if keys[pygame.K_d] and player_class.player_pos.x < (
                SCREEN_WIDTH - player_class.player_size[0]
            ):
                player_class.player_pos.x += VEL * dt

        player_movement()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_g:
                    display_enemies = True

                    SCORE += 1

                    if row_counter < 5:
                        enemy_class.spawn_enemy_row(enemies_list)
                        row_counter += 1

                if event.key == pygame.K_SPACE:
                    # print(
                    #     player_class.player_pos.y,
                    #     player_class.player_pos.x // 2,
                    # )
                    bullet = pygame.Rect(
                        (player_class.player_pos.x - 2.5)
                        + (player_class.player_size[0] // 2),
                        player_class.player_pos.y,
                        5,
                        20,
                    )
                    bullets_list.append(bullet)

        screen.blit(background_image, (0, 0))

        score_text = font.render(f"Score: {SCORE}", True, GREEN)
        screen.blit(score_text, SCORE_POS)

        if display_enemies:
            enemy_class.draw_enemy(screen, enemies_list)

        player_class.draw_player(screen)

        bullet_class.handle_bullet(bullets_list)
        bullet_class.draw_bullet(screen, bullets_list)

        pygame.display.update()
        dt = clock.tick(144) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
