import pygame
from constants import *


def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Running = True

    pygame.init

    while Running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(black)
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
