from circleshape import CircleShape
import constants
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, width=2, radius=self.radius)

    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20 ,50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)

        asteroid1.velocity = vector1
        asteroid2.velocity = vector2
