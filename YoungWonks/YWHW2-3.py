import pygame
from time import sleep
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def get_text(msg, color, size):
    fontobj = pygame.font.SysFont('freesans', size)
    return fontobj.render(msg, False, color)

hello_button_rect = pygame.Rect(0, 0, 250, 75)
hello_button_rect.center = (540, 320)
bye_button_rect = pygame.Rect(0, 0, 250, 75)
bye_button_rect.center = (540, 400)

hello_text = get_text('Hello!', WHITE, 75)
bye_text = get_text('Bye!', WHITE, 75)

running = True
hello = False
bye = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hello_button_rect.collidepoint(event.pos):
                hello = True
                bye = False
            elif bye_button_rect.collidepoint(event.pos):
                hello = False
                bye = True
                
    window.fill(BLACK)
    
    pygame.draw.rect(window, GREEN, hello_button_rect)
    pygame.draw.rect(window, RED, bye_button_rect)
    
    if hello:
        window.blit(hello_text, hello_button_rect)
    elif bye:
        window.blit(bye_text, bye_button_rect)
    
    pygame.display.update()


pygame.quit()