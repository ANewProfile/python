import pygame
import random

pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)


class Circle:
    def __init__(self, radius, position, color, mass=0):
        self.radius = radius
        self.position = position
        self.color = color
        self.mass = mass

    def draw(self):
        pygame.draw.circle(window, self.color, self.position, self.radius)


# Create a list of ten circle objects
# Different radii, colors, and positions
circles = []
for _ in range(0, 10):
    circle = Circle(random.randint(1, 300), (random.randint(0, 600), random.randint(
        0, 600)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    circles.append(circle)

for circle in circles:
    circle.draw()
    if circles.index(circle) != 0:
        pygame.draw.line(
            window, WHITE, circles[circles.index(circle)-1].position, circle.position)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
