import pygame
import sys

from game import Game
from lineblock import LineBlock

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GAME = Game(WIDTH, HEIGHT)

running = True

while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
            (event.type == pygame.KEYDOWN and
             event.key == pygame.K_ESCAPE)):
            running = False
        GAME.handleEvent(event)

    screen.fill("grey")

    GAME.update()

    GAME.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
