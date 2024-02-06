import pygame

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

VEL = 1100
BORDER = pygame.Rect(0, 0, screen_width, screen_height)

player_pos = pygame.Vector2(screen_width / 2 - 100, screen_height - 200)

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
    if keys[pygame.K_a] and  player_pos.x - VEL > 0:
        player_pos.x -= VEL * dt
    if keys[pygame.K_d]:
        player_pos.x += VEL * dt

    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 1000

pygame.quit()