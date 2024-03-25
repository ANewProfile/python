import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

sprite = pygame.image.load('YoungWonks/santasprites/png/Idle (1).png')
sprite = pygame.transform.scale(sprite, (600, 600))
sprite_rect = pygame.Rect(0, 0, 600, 600)
sprite_rect.center = (WIDTH//2, HEIGHT//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(BLACK)
    window.blit(sprite, sprite_rect)
    pygame.display.update()


pygame.quit()
