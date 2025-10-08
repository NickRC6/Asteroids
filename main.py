import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import Asteroid

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0
    clock = pygame.time.Clock()
    status = True   
    while status == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if CircleShape.collision_check(obj, player):
                sys.exit("Game Over!")

        pygame.display.flip()


if __name__ == "__main__":
    main()
