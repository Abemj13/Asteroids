import pygame
from circleshape import *
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.health = 3
        self.flash_timer = 0

    def draw(self, screen):
        color = constants.white if self.flash_timer > 0 else constants.neon_red
        pygame.draw.circle(screen, color, self.position, self.radius, 0)
    
    def update(self, dt):
        self.position +=  self.velocity * dt
        if self.flash_timer > 0:
            self.flash_timer -= dt
            
                
                

    def split(self, asteroid_group):
        self.kill()
        constants.KILL_COUNT += 1
        print(constants.KILL_COUNT)
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

    def take_damage(self):
        self.health -= 1
        self.flash_timer = 0.1
        
        