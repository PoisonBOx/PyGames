import random, math, pygame
from pygame.locals import *
import sys

# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")

# load bitmaps
space = pygame.image.load("space.png").convert()
planet = pygame.image.load("planet.png").convert_alpha()
width, height = planet.get_size()

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # draw background
    screen.blit(space, (0, 0))
    screen.blit(planet, (400-width/2, 300-height/2))

    pygame.display.update()