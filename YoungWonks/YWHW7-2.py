import pygame
from math import dist
from time import sleep
pygame.init()

FPS = 60
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

sprite = pygame.image.load('YoungWonks/santasprites/png/Idle (1).png')
sprite = pygame.transform.scale(sprite, (120, 120))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 10, 10)

class Character(pygame.Rect):
    def __init__(self, rect: pygame.Rect):
        super().__init__(rect.x, rect.y, rect.width, rect.height)
        self.hitbox = pygame.Rect(self.x, self.y, self.width-100, self.height-20)

class Circle:
    def __init__(self, radius, color, center):
        self.center = center
        self.radius = radius
        self.color = color
    
    def draw(self):
        pygame.draw.circle(window, self.color, self.center, self.radius)

def show_text(msg, color, size):
    fontobj = pygame.font.SysFont('freesans', size)
    return fontobj.render(msg, False, color)

game_over_text = show_text('Game Over!', RED, 50)

sprite_rect = Character(pygame.Rect(0, 0, 120, 120))
sprite_rect.hitbox.center = (WIDTH / 3, HEIGHT / 2)

circle = Circle(300, WHITE, (0, 0))
circle.center = (WIDTH * 2/3, HEIGHT / 2)

running = True
right = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if right:
        sprite_rect.hitbox.move_ip(5, 0)

    sprite_rect.center = sprite_rect.hitbox.center


    window.fill(BLACK)

    window.blit(sprite, sprite_rect)
    circle.draw()
    if dist(circle.center, sprite_rect.hitbox.center) < circle.radius:
        window.blit(game_over_text, (WIDTH//2, HEIGHT//2))
        pygame.display.update()
        sleep(2)
        running = False

    pygame.display.update()

pygame.quit()
