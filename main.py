# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import * # import constants 
from player import Player # import the Player class

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set the screen size
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_clock = pygame.time.Clock() #
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create a player at the center of the screen

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = game_clock.tick(60) / 1000 # Convert milliseconds to seconds and cap at 60 FPS
        updatable.update(dt)
        screen.fill((0, 0, 0))  # Fill the screen with black
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()  # Update the display
        
        
if __name__ == "__main__":
    main()
