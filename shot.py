from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,radius, rotation):
        super().__init__(x,y,radius)
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, width=2, radius=self.radius)

    def update(self,dt):
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += constants.PLAYER_SHOOT_SPEED*dt*direction