import pygame

pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Circle:
    def __init__(self, radius, position, color, mass=0):
        self.radius = radius
        self.position = position
        self.color = color
        self.mass = mass
    
    def draw(self):
        pygame.draw.circle(window, self.color, self.position, self.radius)

class Square:
    def __init__(self, length, position, color, mass=0):
        self.length = length
        self.position = position
        self. color = color
        self. mass = mass
    
    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.length, self.length))

class Triangle:
    def __init__(self, position, color, mass=0):
        self.position = position
        self.color = color
        self.mass = mass
    
    def draw(self):
        pygame.draw.polygon(window, self.color, (self.position[0], self.position[1], self.position[2]))

circle = Circle(16, (32, 32), WHITE)
square = Square(16, (1048, 32), WHITE)
triangle = Triangle(((32, 688), (48, 688), (40, 672)), WHITE)
circle.draw()
square.draw()
triangle.draw()
pygame.draw.line(window, WHITE, (1048, 688), (1048, 668))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()