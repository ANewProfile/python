import pygame
from random import randint
pygame.init()

FPS = 30
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class Circle:
    def __init__(self, radius, pos):
        self.radius = radius
        self.pos = pos
    
    def draw(self):
        pygame.draw.circle(window, GREEN, self.pos, self.radius)

class BouncyRectangle(pygame.Rect):
    def __init__(self, rect_width, rect_height, rect_left, rect_top):
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect_left = rect_left
        self.rect_top = rect_top
    
    def draw(self):
        pygame.draw.rect(window, BLUE, (self.rect_left, self.rect_top, self.rect_width, self.rect_height))


bouncing_circle = Circle(50, (540, 360))
bouncy_rect1 = BouncyRectangle(70, 300, randint(0, 1010), randint(0, 420))
bouncy_rect2 = BouncyRectangle(400, 50, randint(0, 608), randint(0, 670))
bouncy_rect3 = BouncyRectangle(235, 175, randint(0, 773), randint(0, 440))

clock = pygame.time.Clock()
bouncing = (True, 1)
bounce_count = 0
direction = 2
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    if bouncing[0]:
        bounce_count += 1
        if bounce_count % 20 == 0:
            bouncing = (0, None)
        else:
            if bouncing[1] == 1:
                # Bounce North
                direction = 1
                bouncing_circle.pos = (bouncing_circle.pos[0], bouncing_circle.pos[1]-5)
            elif bouncing[1] == 2:
                # Bounce East
                direction = 2
                bouncing_circle.pos = (bouncing_circle.pos[0]+5, bouncing_circle.pos[1])
            elif bouncing[1] == 3:
                # Bounce South
                direction = 3
                bouncing_circle.pos = (bouncing_circle.pos[0], bouncing_circle.pos[1]+5)
            elif bouncing[1] == 4:
                # Bounce West
                direction = 4
                bouncing_circle.pos = (bouncing_circle.pos[0]-5, bouncing_circle.pos[1])
            else:
                print('You should never see this!')
                running = False
    else:
        if direction == 1:
            bouncing_circle.pos = (bouncing_circle.pos[0], bouncing_circle.pos[1]-randint(0, 10))
        elif direction == 2:
            bouncing_circle.pos = (bouncing_circle.pos[0]+randint(0, 10), bouncing_circle.pos[1])
        elif direction == 3:
            bouncing_circle.pos = (bouncing_circle.pos[0], bouncing_circle.pos[1]+randint(0, 10))
        elif direction == 4:
            bouncing_circle.pos = (bouncing_circle.pos[0], bouncing_circle.pos[1]+randint(0, 10))
        else:
            print('You should never see this!')
            running = False

    window.fill(BLACK)

    bouncy_rect1.draw()
    bouncy_rect2.draw()
    bouncy_rect3.draw()
    bouncing_circle.draw()

    pygame.display.update()


pygame.quit()
