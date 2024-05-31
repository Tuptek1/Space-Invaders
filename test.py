import pygame


def main():
    time_elapsed_since_last_action = 0
    clock = pygame.time.Clock()

    while True:  # game loop
        # the following method returns the time since its last call in milliseconds
        # it is good practice to store it in a variable called 'dt'
        dt = clock.tick()

        time_elapsed_since_last_action += dt
        # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
        if time_elapsed_since_last_action > 250:
            print(time_elapsed_since_last_action)  # move the snake here
            time_elapsed_since_last_action = 0  # reset it to 0 so you can count again


if __name__ == "__main__":
    main()
