import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 10

image_width = 360
image_height = 360

idle_right = []
for image in range(1, 11):
    sprite = pygame.image.load(f'YoungWonks/platformer_game/png/dog/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    idle_right.append(sprite)

idle_left = []
for image in range(1, 11):
    sprite = pygame.image.load(f'YoungWonks/platformer_game/png/dog/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    sprite = pygame.transform.flip(sprite, True, False)
    idle_left.append(sprite)

idle_left_rect = pygame.Rect(0, 0, image_width, image_height)
idle_right_rect = pygame.Rect(WIDTH-image_width, 0, image_width, image_height)

clock = pygame.time.Clock()
running = True
current_sprite = 0
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(idle_left[current_sprite%10], idle_left_rect)
    window.blit(idle_right[current_sprite%10], idle_right_rect)
    current_sprite += 1
    
    pygame.display.update()


pygame.quit()