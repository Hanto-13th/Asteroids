import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #override by subclasse
        pass

    def update(self, dt):
        #override by subclasse
        pass

    def collide(self,other_object): #method to detect collide with the player or player shot
        distance_between_objects = pygame.Vector2.distance_to(self.position,other_object.position)
        if distance_between_objects > (self.radius + other_object.radius):
            return False
        else:
            return True