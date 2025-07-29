from circleshape import *
from constants import *
from shots import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y, radius, health):
        super().__init__(x, y, PLAYER_RADIUS)
    
        self.rotation = 0
        self.health = health
        self.bullet_timer = 0
        self.invincability_timer = 0
        self.is_colliding = False
    
    def update(self, dt):

        keys = pygame.key.get_pressed()
        self.bullet_timer -= dt
        self.invincability_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
    
    def draw(self, screen):
         # Choose color based on collision state
        color = white if self.is_colliding else neon_blue  # White if colliding, neon_blue otherwise
        pygame.draw.polygon(screen, color, self.triangle(), 0)

    def rotate(self,  dt):
        self.rotation +=  PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOTING_SPEED
        return Shot(self.position.x, self.position.y, SHOT_RADIUS, shot_velocity)

    

