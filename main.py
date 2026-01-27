import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event

def main():
    pygame.init()
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    # Grouping sprites
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for draw in drawable:
            draw.draw(screen)

        for update in updateable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        #player.update(dt)
        #player.draw(screen)

        pygame.display.flip()
        dt = clock.tick() / 1000


if __name__ == "__main__":
    main()
