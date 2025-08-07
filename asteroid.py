import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        exit_angle = random.uniform(20, 50)
        child1_velocity = self.velocity.rotate(exit_angle)
        child2_velocity = self.velocity.rotate(exit_angle * -1)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child2 = Asteroid(self.position.x, self.position.y, child_radius)
        child1.velocity = child1_velocity * 1.2
        child2.velocity = child2_velocity * 1.2