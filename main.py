import pygame
import sys
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
    score = 0
    pclock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables,drawables)
    Asteroid.containers = (asteroids,updatables,drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots,drawables,updatables)
    p1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    af = AsteroidField()




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatables:
            obj.update(dt)
        for asteroid in asteroids:
            if p1.collides(asteroid):
                print(f"Game Over! Final score: {score}")
                sys.exit()
            for shot in shots:
                if shot.collides(asteroid):
                    score += asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()
        dt = pclock.tick(60)/1000



        

if __name__ == "__main__":
    main()