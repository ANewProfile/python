import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

img_w = 150
img_h = 150

img = pygame.image.load('YoungWonks/arrow_through_apple.png')
img = pygame.transform.scale(img, (img_w, img_h))

img_rect = pygame.Rect(0, 0, img_w, img_h)
img_rect.center = (WIDTH//2, HEIGHT//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT):
                if event.key == pygame.K_UP:
                    img_h += 5
                    img_rect.height += 5
                elif event.key == pygame.K_RIGHT:
                    img_w += 5
                    img_rect.width += 5
                elif event.key == pygame.K_DOWN:
                    img_h -= 5
                    img_rect.height -= 5
                elif event.key == pygame.K_LEFT:
                    img_w -= 5
                    img_rect.width -= 5
    
    
    img = pygame.transform.scale(img, (img_w, img_h))
    img_rect.center = (WIDTH//2, HEIGHT//2)
    
    window.fill(BLACK)
    
    window.blit(img, img_rect)
    
    pygame.draw.rect(window, WHITE, img_rect, 5)
    
    pygame.display.update()

pygame.quit()