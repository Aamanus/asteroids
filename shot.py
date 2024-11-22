import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):

    containers = ()

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)  # Initialize the CircleShape with position and radius
        self.velocity = velocity  # Set the bullet's velocity

    def update(self,dt):
        # Update the position of the shot based on its velocity
        self.position += self.velocity * dt

    def draw(self, surface):
        # Draw the shot on the given surface
        pygame.draw.circle(surface, (255, 0, 0), self.position, self.radius,2)
