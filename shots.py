import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x , y, radius)
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, neon_blue, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position +=  self.velocity * dt

    
        