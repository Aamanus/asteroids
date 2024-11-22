import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pclock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables,drawables)
    p1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatables:
            obj.update(dt)
        screen.fill((0, 0, 0))
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()
        dt = pclock.tick(60)/1000



        

if __name__ == "__main__":
    main()