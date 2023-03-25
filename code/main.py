import pygame, sys
from random import randint, uniform
from settings import *
from player import Player
from car import Car

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.bg = pygame.image.load('graphics/main/map.png').convert()
        self.fg = pygame.image.load('graphics/main/overlay.png').convert_alpha()

    def customize_draw(self):

        display_surface.blit(self.bg, (0, 0))
        display_surface.blit(self.fg, (0, 0))         

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            display_surface.blit(sprite.image, offset_pos)

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger-like")
clock = pygame.time.Clock()

# groups
all_sprites = AllSprites()

# sprites
player = Player((WINDOW_WIDTH  /2, WINDOW_HEIGHT /2), all_sprites)
car = Car((100, 200), all_sprites)

# game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # draw a background
    display_surface.fill('black')

    # update
    all_sprites.update(dt)

    # draw
    all_sprites.customize_draw()

    # update the display surface
    pygame.display.update()