import pygame
pygame.init()

FPS = 20
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)

walking_right = []
for image in range(1, 11):
    sprite = pygame.image.load(f'python/YoungWonks/png 2/male/Walk ({image}).png')
    walking_right.append(sprite)

current_sprite = 0
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(BLACK)
    window.blit(walking_right[current_sprite%10], (0, 0))
    current_sprite += 1
    pygame.display.update()


pygame.quit()