import pygame
from circleshape import *
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.health = 3

        self.flash_timer = 0

        self.dying = False
        self.death_timer = 0


    def draw(self, screen):
        color = constants.white if self.flash_timer > 0 else constants.grey_purple
        pygame.draw.circle(screen, color, self.position, self.radius, 0)
        pygame.draw.circle(screen, constants.neon_purple, self.position, self.radius - 5, 5)
        pygame.draw.circle(screen, constants.white, self.position, self.radius, 5)
        pygame.draw.circle(screen, constants.neon_purple, self.position, self.radius + 5, 5)
        
        
    
    def update(self, dt):
        self.position +=  self.velocity * dt
        if self.flash_timer > 0:
            self.flash_timer -= dt
        if self.dying:
            self.death_timer -= dt
            if self.death_timer <= 0:
                self.kill()

    def split(self, asteroid_group):
        
        constants.KILL_COUNT += 1
        self.dying = True #this fixed my problem of the asteroids not flashing when hit to 0 hp. 
        
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(30,50)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            for i in range (-1, constants.ASTEROID_SPLIT_COUNT + 1, 2):
                velocity_i = self.velocity.rotate(i*random_angle)           
                new_asteroid_i = Asteroid(self.position.x, self.position.y, new_radius)
                new_asteroid_i.velocity = velocity_i * 1.5
                asteroid_group.add(new_asteroid_i)

        
        
    def take_damage(self, dt):
        self.health -= 1
        self.flash_timer = 0.1
        if self.health <= 0:
            self.dying = True
            self.death_timer = dt
        
        