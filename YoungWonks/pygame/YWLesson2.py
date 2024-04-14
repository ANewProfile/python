import pygame
import random
from math import dist
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

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
        percentage = (index/list_count) * 100
        if percentage >= 90:
            self.color = (255, 255, 255)
        elif percentage in range(80, 90):
            self.color = (230, 230, 230)
        elif percentage in range(70, 80):
            self.color = (204, 204, 204)
        elif percentage in range(60, 70):
            self.color = (179, 179, 179)
        elif percentage in range(50, 60):
            self.color = (153, 153, 153)
        elif percentage in range(40, 50):
            self.color = (128, 128, 128)
        elif percentage in range(30, 40):
            self.color = (102, 102, 102)
        elif percentage in range(20, 30):
            self.color = (77, 77, 77)
        elif percentage in range(10, 20):
            self.color = (51, 51, 51)
        elif percentage in range(0, 10):
            self.color = (26, 26, 26)
        
        print(self.color)


circles = {'a': Circle(50, WHITE, (random.randint(50, 1030), random.randint(50, 680))), 'b': Circle(45, YELLOW, (random.randint(50, 1030), random.randint(50, 680))),
             'c': Circle(25, BLUE, (random.randint(50, 1030), random.randint(50, 680))), 'd': Circle(5, RED, (random.randint(50, 1030), random.randint(50, 680)))}


clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FRAMERATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_pos = event.pos
        #     reversed_circles = circles[::-1]
        #     for circle in reversed_circles:
        #         if circle.check_distance(mouse_pos) <= circle.radius:
        #             reversed_circles.remove(circle)
        #             break
            # 
            # circles = reversed_circles[::-1]

    window.fill(BLACK)
    for circle, object in circles.items():
        if object.radius <= 5:

            if circle == 'a':
                radius = 50
                color = WHITE
            elif circle == 'b':
                radius = 45
                color = YELLOW
            elif circle == 'c':
                radius = 25
                color = BLUE
            else:
                radius = 5
                color = RED

            new_circle = Circle(radius, color, (random.randint(radius, WIDTH-radius), random.randint(radius, HEIGHT-radius)))
            circles[circle] = new_circle
        
        object.shrink(0.1)

        # try:
        #     circle.change_color(circles.index(circle), len(circles))
        # except ValueError:
        #     pass

        object.draw()

    pygame.display.update()

pygame.quit()
