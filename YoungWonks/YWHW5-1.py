import pygame
pygame.init()

FPS = 50
WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Square:
    def __init__(self, square_length, square_width, square_x, square_y) -> None:
        self.square_length = square_length
        self.square_width = square_width
        self.square_x = square_x
        self.square_y = square_y
    
    def draw(self):
        pygame.draw.rect(window, WHITE, pygame.Rect(self.square_x, self.square_y, self.square_width, self.square_length))

bottom_left = Square(50, 50, 0, 450)
top_right = Square(50, 50, 450, 0)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update bottom left square
    bottom_left.square_x += 1
    bottom_left.square_y -= 1

    # Update top right square
    top_right.square_x -= 1
    top_right.square_y += 1

    window.fill(BLACK)
    top_right.draw()
    bottom_left.draw()
    pygame.display.update()


pygame.quit()