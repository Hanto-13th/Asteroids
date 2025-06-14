import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    FPS = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    
        screen.fill((0,0,0))

        for element in drawable:
            element.draw(screen)
        updatable.update(dt)
        for object in asteroids:
            if player.collide(object) == True:
                print("Game Over")
                running = False

        pygame.display.flip()

    
        dt = FPS.tick(60) /1000

if __name__ == "__main__":
    main()


