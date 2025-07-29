import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #staticfields
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    #members?
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, PLAYER_HP)
    asteroidfield = AsteroidField()

    dt = 0

    while True:

        for event in pygame.event.get():

           

            if event.type == pygame.QUIT:
                return
            
        keys = pygame.key.get_pressed()  

        if keys[pygame.K_SPACE]:
            shot = player.shoot()
            shots.add(shot)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                player.health -= 1
                print(f"Ouch! Whatch those asteroids Joe, you have {player.health} remaining lives!")
                
            if player.health <= 0:
                sys.exit()

        screen.fill(neon_purple)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        
        

if __name__ == "__main__":
    main()
