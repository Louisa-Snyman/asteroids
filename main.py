import pygame, sys
from constants import *
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    new_astroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (new_astroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (all_shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in new_astroids:
            if asteroid.collision(player):
                print ("Game over!")
                sys.exit()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()