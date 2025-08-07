# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import * # import constants 
from player import Player # import the Player class
from asteroidfield import AsteroidField # import AsteroidField class
from asteroid import Asteroid
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set the screen size
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_clock = pygame.time.Clock() #
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create a player at the center of the screen
    asteroid_field = AsteroidField()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = game_clock.tick(60) / 1000 # Convert milliseconds to seconds and cap at 60 FPS
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()  # Update the display
        
        
if __name__ == "__main__":
    main()
