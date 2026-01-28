import pygame
import random
from typing import override
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        # Split into two asteroids
        vector_01 = self.velocity.rotate(angle)
        vector_02 = self.velocity.rotate(-angle)
        
        # Compute new radius for each asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        aster_01 = Asteroid(self.position.x, self.position.y, new_radius)
        aster_02 = Asteroid(self.position.x, self.position.y, new_radius)

        aster_01.velocity = vector_01 * 1.2
        aster_02.velocity = vector_02 * 1.2
