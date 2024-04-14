import pygame
from random import randint

pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Square:
    def __init__(self, length, position, color, mass=0):
        self.length = length
        self.position = position
        self. color = color
        self. mass = mass
    
    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.length, self.length))

x = randint(1, 1080)
y = randint(1, 720)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)
    square = Square(32, (x, y), WHITE)
    square.draw()

    if x < 1:
        x = 1080
    x -= 1

    pygame.display.update()

pygame.quit()