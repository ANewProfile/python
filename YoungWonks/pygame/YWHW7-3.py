import pygame
pygame.init()

FPS = 60
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
        self.moving_left = False
    
    def draw(self):
        pygame.draw.circle(window, self.color, self.center, self.radius)


circle = Circle(50, WHITE, (WIDTH // 3, HEIGHT // 2))

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if circle.moving_left:
        if circle.center[0] - circle.radius <= 0:
            circle.moving_left = False
        else:
            circle.center = (circle.center[0]-5, circle.center[1])
    else:
        if circle.center[0] + circle.radius >= WIDTH:
            circle.moving_left = True
        else:
            circle.center = (circle.center[0]+5, circle.center[1])
            
    
    window.fill(BLACK)
    
    circle.draw()
    
    pygame.display.update()


pygame.quit()
