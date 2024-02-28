import pygame
from random import randint
pygame.init()

FPS = 60
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Square:
    def __init__(self, square_length, square_width, square_x, square_y, color):
        self.square_length = square_length
        self.square_width = square_width
        self.square_x = square_x
        self.square_y = square_y
        self.color = color
    
    def draw(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.square_x, self.square_y, self.square_width, self.square_length))

square = Square(75, 75, 502, 322, WHITE)
screen_color = BLACK
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            if mouse_x in range(502, 578):
                if mouse_y in range(322, 398):
                    square.color = (randint(0, 255), randint(0, 255), randint(0, 255))
                else:
                    screen_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            else:
                screen_color = (randint(0, 255), randint(0, 255), randint(0, 255))


    window.fill(screen_color)
    square.draw()
    pygame.display.update()


pygame.quit()