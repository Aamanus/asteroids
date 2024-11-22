import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):

    containers = ()
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)
        if keys[pygame.K_a]:
            self.rotate(0-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self,dt):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        if self.shoot_cooldown > 0:
            return
        # Create a new pygame.Vector2 for the initial velocity
        initial_velocity = pygame.Vector2(0, 1)  # Start with a vector pointing downwards

        # Rotate the vector to match the player's direction
        rotated_velocity = initial_velocity.rotate(self.rotation)

        # Scale the velocity to make it move faster
        final_velocity = rotated_velocity * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        # Create the shot
        return Shot(self.position[0], self.position[1], final_velocity)