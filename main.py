import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys

pygame.init()


def main():
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    gamezone = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"'Starting Asteroids' with pygame version: {pygame.version.ver}")
    print(f"'Screen width: {SCREEN_WIDTH}'")
    print(f"'Screen height: {SCREEN_HEIGHT}'")
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    controller = Player(x, y)
    while(1==1):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt) 
        for member in drawable:
            member.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()

            if controller.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for shot in shots:
            shot.draw(screen)
            shot.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
