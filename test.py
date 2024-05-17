import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# I changed the background color to black, because I understood it as that is what you want.
BACKGROUND_COLOR = (0, 0, 0)  # tausta_vari

clock = pygame.time.Clock()  # kello
star = pygame.Surface((32, 32))
star.fill((255, 255, 255))

planets = random.randrange(100, 500)
positions = [(300, 50), (400, 27), (900, 55)]

WIDTH, HEIGHT = (1000, 1000)  # (leveys, korkeus)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # ikkuna
pygame.display.set_caption("SpaceGenerationTest")

display_stars = False
running = True  # toiminnassa
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                print("Generating World....")
                print(planets)
                display_stars = True

    screen.fill(BACKGROUND_COLOR)

    if display_stars:
        for position in positions:
            # This will create 3 stars because there're 3 elements in the list positions.
            # To create more stars you'll need to add more in the list positions.
            screen.blit(star, position)

    pygame.display.update()
