import pygame

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

pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, 5))
    # Draw bottom border
pygame.draw.rect(screen, BLACK, (0, SCREEN_WIDTH - 5, SCREEN_WIDTH, 5))
    # Draw left border
pygame.draw.rect(screen, BLACK, (0, 0, 5, SCREEN_WIDTH))
    # Draw right border
pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - 5, 0, 5, SCREEN_WIDTH))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    imp = pygame.image.load('./dd4af67c-c3f1-434e-9dad-659ef705893e.png').convert()
    imp = pygame.transform.scale(imp, (200, 200))
    
    shipRect = pygame.rect
    screen.blit(imp, (player_pos, imp.get_size()))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= VEL * dt
    if keys[pygame.K_s]:
        player_pos.y += VEL * dt
    if keys[pygame.K_a]:
        player_pos.x -= VEL * dt
    if keys[pygame.K_d]:
        player_pos.x += VEL * dt

    player_pos.x = max(0, min(player_pos.x, SCREEN_WIDTH - 200))
    player_pos.y = max(0, min(player_pos.y, SCREEN_HEIGHT - 200))

    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 1000

pygame.quit()