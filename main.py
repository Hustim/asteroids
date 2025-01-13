# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
         for thing in updatable:
             thing.update(dt)
         pygame.Surface.fill(screen, (0, 0, 0))
         for thing in drawable:
             thing.draw(screen)
         for asteroid in asteroids:
             if asteroid.collision_check(player):
                 print("Game over!")
                 return
             for shot in shots:
                 if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
                 
         pygame.display.update()
         dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()