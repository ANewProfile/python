import pygame
from random import randint
pygame.init()


FPS = 30
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)

image_width = 360
image_height = 360

idle_right = []
for image in range(1, 11):
    sprite = pygame.image.load(f'python/YoungWonks/adventure_girl_pngs/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    idle_right.append(sprite)

image_rect = pygame.Rect(360, 180, image_width, image_height)
current_sprite = 0

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    window.fill(BLACK)

    window.blit(idle_right[current_sprite%10], image_rect)
    current_sprite += 1

    scale_by = randint(-5, 5)
    # scale_by = 5
    image_width += scale_by
    image_height += scale_by

    image_rect.scale_by_ip(scale_by, scale_by)
    print(f'image_rect.scale_by_ip({scale_by}, {scale_by})')
    for sprite in idle_right:
        sprite = pygame.transform.scale(sprite, (image_width, image_height))
        print(f'sprite = pygame.transform.scale(sprite, ({image_width}, {image_height}))')

    pygame.display.update()

pygame.quit()