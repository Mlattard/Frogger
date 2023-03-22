import pygame, sys
from random import randint, uniform
from settings import *

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger-like")
clock = pygame.time.Clock()

# background
background_surface = pygame.image.load('graphics/background.png').convert()

# game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # backgrounds
    display_surface.blit(background_surface, (0,0))

    # update the display surface
    pygame.display.update()