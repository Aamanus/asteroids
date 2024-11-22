import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):

        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        score = int(10 * (self.radius/ASTEROID_MIN_RADIUS) * self.velocity.length())
        if self.radius == ASTEROID_MIN_RADIUS:
            return score
        rotation = random.uniform(20,50)
        rotation1 = self.velocity.rotate(rotation)
        rotation2 = self.velocity.rotate(-rotation)
        new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = rotation1 * 1.2
        new_asteroid2.velocity = rotation2 * 1.2
        
        return score
        
        