import pygame
import math
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Pentagon:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def draw(self):
        pygame.draw.polygon(window, self.color, [(self.x-self.radius/2, self.y-self.radius), (self.x+self.radius/2, self.y-self.radius), (self.x+self.radius, self.y), (self.x, self.y+self.radius), (self.x-self.radius, self.y)])

pentagon = Pentagon(WIDTH//2, HEIGHT//2, WHITE, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(BLACK)
    pentagon.draw()
    pygame.display.update()

pygame.quit()
