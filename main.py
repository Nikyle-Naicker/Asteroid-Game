import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

pygame.init()


def main():
    dt = 0
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
        controller.update(dt)
        Player.draw(controller, screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
