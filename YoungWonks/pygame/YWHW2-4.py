import pygame
pygame.init()

FPS = 30
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def get_text(msg, color, size):
    fontobj = pygame.font.SysFont('freesans', size)
    return fontobj.render(msg, False, color)

ad_text = get_text('YoungWonks Hackathon coming next month!', WHITE, 75)
ad_rect = pygame.Rect(0, 0, 1200, 75)
ad_rect.center = (0, 360)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if ad_rect.left >= 1080:
        ad_rect.right = 0
    else:
        ad_rect.center = (ad_rect.center[0]+5, ad_rect.center[1])
    
    window.fill(BLACK)
    
    window.blit(ad_text, ad_rect)
    
    pygame.display.update()


pygame.quit()