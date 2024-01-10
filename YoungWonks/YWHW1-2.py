import pygame
from random import randint
from time import sleep
from math import hypot

pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Circle:
    def __init__(self, radius, position, color, mass=0, hovering=False):
        self.radius = radius
        self.position = position
        self.color = color
        self.original_color = color
        self.mass = mass
        self.hovering = hovering
        print(self.color)
        print(self.original_color)

    def draw(self):
        pygame.draw.circle(window, self.color, self.position, self.radius)
    
    def check_hovering(self):
        if self.hovering:
            self.color = WHITE
            self.hovering = False
        else:
            self.color = self.original_color


# Create a list of ten circle objects
# Different radii, colors, and positions
circles = []
for _ in range(0, 10):
    circle = Circle(randint(1, 300), (randint(0, 600), randint(
        0, 600)), (randint(0, 255), randint(0, 255), randint(0, 255)))

    circles.append(circle)
    circle.draw()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    for circle in circles:
        dist_x = mouse_pos[0] - circle.position[0]
        dist_y = mouse_pos[1] - circle.position[1]
        if hypot(dist_x, dist_y) <= circle.radius:
            circle.hovering = True
        
        circle.check_hovering()
    
    window.fill(BLACK)
    for circle in circles:
        circle.draw()

    pygame.display.update()

pygame.quit()
