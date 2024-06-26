import random
import pygame
from player_bullet import Bullet
from enemy import Enemy
from player import Player
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
font = pygame.font.Font("freesansbold.ttf", 32)

player_class = Player()
bullet_class = Bullet()
enemy_class = Enemy()


def main():
    clock = pygame.time.Clock()
    SCORE = 0
    HEALTH = 10
    row_counter = 0
    running = True

    background_image = pygame.image.load(BACKGROUND_IMAGE).convert()
    player_bullets_list = []
    enemy_bullets_list = []
    enemy_pos_list = enemy_class.enemy_pos_list

    while running:
        if HEALTH == 0:
            running = False

        for bullet in player_bullets_list:
            for enemy in enemy_pos_list:
                if pygame.rect.Rect.colliderect(bullet, enemy[1]):
                    SCORE += 1
                    player_bullets_list.remove(bullet)
                    enemy_class.enemy_pos_list.remove(enemy)

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

        if not enemy_pos_list:
            enemy_class.enemy_pos = (40, -70)
            row_counter = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    enemy_class.enemy_shoot(enemy_pos_list, enemy_bullets_list)

                if event.key == pygame.K_g:
                    if row_counter < 5:
                        enemy_class.move_enemy_y()
                        enemy_class.enemy_pos = (40, enemy_class.enemy_pos[1])
                        row_counter += 1

                        if row_counter == 2:
                            enemy_image = pygame.image.load(
                                ENEMY_DRAGON_PATH_1
                            ).convert()
                            enemy_image = pygame.transform.scale(
                                enemy_image, enemy_class.enemy_size
                            )
                            for _ in range(12):
                                enemy_rect = enemy_image.get_rect(
                                    topleft=enemy_class.enemy_pos
                                )
                                enemy_pos_list.append(
                                    (enemy_class.enemy_pos, enemy_rect, enemy_image)
                                )
                                enemy_class.move_enemy_x()

                        if row_counter == 3:
                            enemy_image = pygame.image.load(ENEMY_MAGE_PATH_1).convert()
                            enemy_image = pygame.transform.scale(
                                enemy_image, enemy_class.enemy_size
                            )

                            for _ in range(12):
                                enemy_rect = enemy_image.get_rect(
                                    topleft=enemy_class.enemy_pos
                                )
                                enemy_pos_list.append(
                                    (enemy_class.enemy_pos, enemy_rect, enemy_image)
                                )
                                enemy_class.move_enemy_x()

                        if row_counter == 4 or row_counter == 5:
                            enemy_image = pygame.image.load(
                                ENEMY_GUARD_PATH_1
                            ).convert()
                            enemy_image = pygame.transform.scale(
                                enemy_image, enemy_class.enemy_size
                            )

                            for _ in range(12):
                                enemy_rect = enemy_image.get_rect(
                                    topleft=enemy_class.enemy_pos
                                )
                                enemy_pos_list.append(
                                    (enemy_class.enemy_pos, enemy_rect, enemy_image)
                                )
                                enemy_class.move_enemy_x()

                if event.key == pygame.K_SPACE:

                    player_bullet = pygame.Rect(
                        (player_class.player_pos.x - 2.5)
                        + (player_class.player_size[0] // 2),
                        player_class.player_pos.y,
                        5,
                        20,
                    )

                    player_bullets_list.append(player_bullet)

        screen.blit(background_image, (0, 0))

        score_text = font.render(f"Score: {SCORE}", True, GREEN)
        health_text = font.render(f"Health: {HEALTH}", True, RED)
        screen.blit(score_text, SCORE_POS)
        screen.blit(health_text, HEALTH_POS)

        player_class.draw_player(screen)

        enemy_class.draw_enemies(enemy_pos_list, screen)

        bullet_class.handle_enemy_bullet(enemy_bullets_list)
        bullet_class.handle_player_bullet(player_bullets_list)
        bullet_class.draw_bullet(screen, player_bullets_list, enemy_bullets_list)

        pygame.display.update()
        dt = clock.tick(144) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
