import pygame
from random import randint
from math import dist
pygame.init()


FPS = 30
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Circle:
    def __init__(self, radius, center, color):
        self.radius = radius
        self.center = center
        self.color = color
    
    def draw(self):
        pygame.draw.circle(window, self.color, self.center, self.radius)

circle = Circle(15, (0, 0), WHITE)
square = pygame.Rect(randint(20, WIDTH-20), randint(20, HEIGHT-20), 40, 40)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    circle.center = pygame.mouse.get_pos()
    
    if dist(circle.center, square.topleft) <= circle.radius or dist(circle.center, square.topright) <= circle.radius or \
       dist(circle.center, square.bottomleft) <= circle.radius or dist(circle.center, square.bottomright) <= circle.radius:
           circle.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    
    window.fill(BLACK)
    
    pygame.draw.rect(window, WHITE, square)
    circle.draw()
    
    pygame.display.update()


pygame.quit()