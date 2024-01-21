import pygame
import random
from math import dist
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FRAMERATE = 60

class Circle:
    def __init__(self, radius, color, position):
        self.radius = radius
        self.color = color
        self.position = position
    
    def draw(self):
        pygame.draw.circle(window, self.color, self.position, self.radius)
    
    def shrink(self, amount):
        self.radius -= amount
    
    def check_distance(self, pos):
        return dist(self.position, pos)

    def change_color(self, index, list_count):
        pass


circles = []
for _ in range(100):
    radius = random.randint(20, 40)
    circle = Circle(radius, WHITE, (random.randint(radius, WIDTH-radius), random.randint(radius, HEIGHT-radius)))
    circles.append(circle)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FRAMERATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            reversed_circles = circles[::-1]
            for circle in reversed_circles:
                if circle.check_distance(mouse_pos) <= circle.radius:
                    reversed_circles.remove(circle)
                    break
            
            circles = reversed_circles[::-1]

    window.fill(BLACK)
    for circle in circles:
        if circle.radius <= 5:
            circles.remove(circle)
            radius = random.randint(20, 40)
            new_circle = Circle(radius, WHITE, (random.randint(radius, WIDTH-radius), random.randint(radius, HEIGHT-radius)))
            circles.insert(0, new_circle)
        
        circle.shrink(0.1)
        circle.draw()

    pygame.display.update()

pygame.quit()
