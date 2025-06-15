import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape): #creation of asteroid class
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self): #split to kill them with player shoot him
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        velocity_1 = self.velocity.rotate(random_angle)
        velocity_2 = self.velocity.rotate(-random_angle)
        self.radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x,self.position.y,self.radius)
        new_asteroid2 = Asteroid(self.position.x,self.position.y,self.radius)
        new_asteroid1.velocity = velocity_1
        new_asteroid2.velocity = velocity_2


