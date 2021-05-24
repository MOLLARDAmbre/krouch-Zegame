import pygame
import sys
from pygame.locals import *
from ui import UI

def main():
    ui = UI("sane-krouch.png", "insane-krouch.png")
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60
    while True:  # Game loop
        ui.update()
        ui.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    ui.key('q')
                if event.key == pygame.K_w:
                    ui.key('w')
                if event.key == pygame.K_e:
                    ui.key('e')
                if event.key == pygame.K_r:
                    ui.key('r')

        clock.tick(FPS)


if __name__ == "__main__":
    main()
