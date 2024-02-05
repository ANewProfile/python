import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

FRAMERATE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

image_w = 240
image_h = 240

idle_right = []
for image in range(1, 17):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_w, image_h))
    idle_right.append(sprite)

idle_left = []
for image in range(1, 17):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_w, image_h))
    sprite = pygame.transform.flip(sprite, True, False)
    idle_left.append(sprite)

walk_right = []
for image in range(1, 14):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Walk ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_w, image_h))
    walk_right.append(sprite)

walk_left = []
for image in range(1, 14):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Walk ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_w, image_h))
    sprite = pygame.transform.flip(sprite, True, False)
    walk_left.append(sprite)

x = 0
y = 120
speed_x = 10
speed_y = 10

image_rect = pygame.Rect(x, y, image_w, image_h)
hitbox = pygame.Rect(x, y, 50, 50)
wall_right = pygame.Rect(800, 0, 10, 720)

run = True
clock = pygame.time.Clock()
current_sprite = 0
current_list = idle_right
while run:
    clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                current_list = walk_right
                current_sprite = 0
            if event.key == pygame.K_a:
                current_list = walk_left
                current_sprite = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                current_list = idle_right
                current_sprite = 0
            if event.key == pygame.K_a:
                current_list = idle_left
                current_sprite = 0
    
    window.fill(BLACK)
    # Draw Other Shapes
    pygame.draw.rect(window, WHITE, wall_right)

    # Animate Sprite
    window.blit(current_list[current_sprite%len(current_list)], image_rect)
    current_sprite += 1

    # Move Sprite
    if current_list == walk_right:
        hitbox.x += speed_x
        if hitbox.colliderect(wall_right):
            hitbox.right = wall_right.left
    elif current_list == walk_left:
        hitbox.x -= speed_x
    
    image_rect.center = hitbox.center

    pygame.display.update()


pygame.quit()
