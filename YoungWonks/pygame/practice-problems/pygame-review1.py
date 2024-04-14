import pygame
from random import randint
from math import dist
pygame.init()


WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Circle:
    def __init__(self, radius, color, center):
        self.radius = radius
        self.color = color
        self.center = center
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def draw(self):
        pygame.draw.circle(window, self.color, self.center, self.radius)


circles = []
for _ in range(100):
    circle = Circle(20, WHITE, (randint(20, WIDTH-20), randint(20, HEIGHT-20)))
    circles.append(circle)

last_circle_clicked = None

dragging_circle = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for circle in circles:
                    if dist(event.pos, circle.center) <= circle.radius:
                        circle.color = (randint(0, 255), randint(0, 255), randint(0, 255))
                        last_circle_clicked = circle
            elif event.button == 3:
                for circle in circles:
                    if dist(event.pos, circle.center) <= circle.radius:
                        circle.center = event.pos
                        dragging_circle = True
                        last_circle_clicked = circle
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                dragging_circle = False
        elif event.type == pygame.KEYDOWN:
            if last_circle_clicked:
                if event.key == pygame.K_w:
                    last_circle_clicked.moving_up = True
                    last_circle_clicked.moving_down = False
                    last_circle_clicked.moving_left = False
                    last_circle_clicked.moving_right = False
                elif event.key == pygame.K_a:
                    last_circle_clicked.moving_up = False
                    last_circle_clicked.moving_down = False
                    last_circle_clicked.moving_left = True
                    last_circle_clicked.moving_right = False
                elif event.key == pygame.K_s:
                    last_circle_clicked.moving_up = False
                    last_circle_clicked.moving_down = True
                    last_circle_clicked.moving_left = False
                    last_circle_clicked.moving_right = False
                elif event.key == pygame.K_d:
                    last_circle_clicked.moving_up = False
                    last_circle_clicked.moving_down = False
                    last_circle_clicked.moving_left = False
                    last_circle_clicked.moving_right = True
                
                circles[circles.index(last_circle_clicked)] = last_circle_clicked
        elif event.type == pygame.KEYUP:
            if last_circle_clicked:
                last_circle_clicked.moving_up = last_circle_clicked.moving_down = last_circle_clicked.moving_left = last_circle_clicked.moving_right = False
            
                circles[circles.index(last_circle_clicked)] = last_circle_clicked

    if last_circle_clicked:
        if last_circle_clicked.moving_up:
            last_circle_clicked.center = (last_circle_clicked.center[0], last_circle_clicked.center[1]-5)
        elif last_circle_clicked.moving_down:
            last_circle_clicked.center = (last_circle_clicked.center[0], last_circle_clicked.center[1]+5)
        elif last_circle_clicked.moving_right:
            last_circle_clicked.center = (last_circle_clicked.center[0]+5, last_circle_clicked.center[1])
        elif last_circle_clicked.moving_left:
            last_circle_clicked.center = (last_circle_clicked.center[0]-5, last_circle_clicked.center[1])
        
        circles[circles.index(last_circle_clicked)] = last_circle_clicked
    
    
    if dragging_circle:
        last_circle_clicked.center = pygame.mouse.get_pos()
        
        circles[circles.index(last_circle_clicked)] = last_circle_clicked
        
        
    window.fill(BLACK)
    
    for circle in circles:
        circle.draw()
    
    pygame.display.update()


pygame.quit()