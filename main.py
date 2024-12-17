import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.hasCollisioned(shot):
                    shot.kill()
                    asteroid.split()

            if asteroid.hasCollisioned(player):
                print('Game Over!')
                sys.exit()

        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
