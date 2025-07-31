import pygame
import constants
import images
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
import sys
from UI import GameUI


def main():

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    ui = GameUI()


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
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.PLAYER_RADIUS, constants.PLAYER_HP)
    asteroidfield = AsteroidField()
   
    dt = 0

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
        keys = pygame.key.get_pressed()  
        player.is_colliding = False
        
        

        if keys[pygame.K_SPACE]:
            if player.bullet_timer <= 0:
                player.bullet_timer = constants.PLAYER_SHOOT_COOLDOWN
                shot = player.shoot()
                shots.add(shot)
            

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if player.invincability_timer <= 0:
                    player.invincability_timer = constants.PLAYER_INV_FRAMES
                    player.health -= 1
                    player.is_colliding = True
                    print(f"Ouch! Whatch those asteroids Joe, you have {player.health} remaining lives!")

                if player.health <= 0:
                    sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.take_damage(dt)  # Handle damage and flashing
                    shot.kill()
                    if asteroid.health == 0:
                        asteroid.split(asteroids)
                        print(f"KILL_COUNT in main after split: {constants.KILL_COUNT}")  # Add this line
                
        #draw background
        screen.blit(images.background, (0, 0))


        #draw the sprites
        for obj in drawable:
            obj.draw(screen)        

        #draw the ui
        
        ui.draw_stats(screen, player.health, constants.KILL_COUNT)
       

        pygame.display.flip()

        dt = clock.tick(60)/1000
        
        

if __name__ == "__main__":
    main()
