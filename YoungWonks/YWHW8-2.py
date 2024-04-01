import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def make_text(msg, color, size):
    font_obj = pygame.font.SysFont('freesans', size)
    return font_obj.render(msg, False, color)


start_rect = pygame.Rect(0, 0, 250, 75)
start_rect.center = (540, 320)
quit_rect = pygame.Rect(0, 0, 250, 75)
quit_rect.center = (540, 400)

start_text = make_text('START', WHITE, 75)
quit_text = make_text('QUIT', WHITE, 75)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(BLACK)
    
    pygame.draw.rect(window, GREEN, start_rect)
    pygame.draw.rect(window, RED, quit_rect)
    
    window.blit(start_text, start_rect)
    window.blit(quit_text, quit_rect)
    
    pygame.display.update()


pygame.quit()