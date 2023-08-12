import pygame
import sys


size = (480, 640)
screen = pygame.display.set_mode(size)
pygame.init()


# Rectangle class -- inherit from pygame.Rect
class Rectangle(pygame.Rect):
    def __init__(self, x, y, width, height):
        super.__init__()


# Plaer class
class Player:
    ...


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()
