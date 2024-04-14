import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Hexagon:
    def __init__(self, center, color):
        self.center = center
        self.color = color
    
    def draw(self):
        pygame.draw.polygon(window, self.color, ((self.center[0]-25, self.center[1]-25), (self.center[0]+25, self.center[1]-25), (self.center[0]+35, self.center[1]), (self.center[0]+25, self.center[1]+25), (self.center[0]-25, self.center[1]+25), (self.center[0]-35, self.center[1])))

hexagon = Hexagon((-50, -50), WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hexagon.center = event.pos
        
    window.fill(BLACK)
    hexagon.draw()
    pygame.display.update()


pygame.quit()