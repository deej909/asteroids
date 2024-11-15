import pygame
from circleshape import CircleShape
from constants import *
import sys
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            #generate random angle for new split asteroids
            random_angle = random.uniform(20, 50)
            right_split_angle = self.velocity.rotate(random_angle)
            left_split_angle = self.velocity.rotate(-random_angle)
            #reduce radius of new asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            #spawn new asteroids
            right_asteroid = Asteroid(self.position.x, self.position.y,new_radius)
            left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            right_asteroid.velocity = right_split_angle * 1.2
            left_asteroid.velocity = left_split_angle * 1.2
            self.kill()

        