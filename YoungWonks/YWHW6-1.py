import pygame
pygame.init()


WIDTH = 1080
HEIGHT = 1080
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)


width = 1080
height = 1080
image = pygame.image.load('python/YoungWonks/arrow_through_apple.png')
image = pygame.transform.scale(image, (width, height))
image_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                width += 5
                height += 5
                image = pygame.transform.scale(image, (width, height))
                print('Size up')
            elif event.key == pygame.K_DOWN:
                width -= 5
                height -= 5
                image = pygame.transform.scale(image, (width, height))
                print('Size down')
            elif event.key == pygame.K_SPACE:
                image = pygame.transform.flip(image, True, False)
                print('Flipping')
    
    window.fill(BLACK)
    window.blit(image, image_rect)
    pygame.display.update()

pygame.quit()