import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 20

BLACK = (0, 0, 0)

image_width = 120
image_height = 120

idle_right = []
for image in range(1, 11):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    idle_right.append(sprite)
print(len(idle_right))

idle_left = []
for image in range(1, 11):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    sprite = pygame.transform.flip(sprite, True, False)
    idle_left.append(sprite)

walk_right = []
for image in range(1, 11):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Walk ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    walk_right.append(sprite)

walk_left = []
for image in range(1, 11):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Walk ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    sprite = pygame.transform.flip(sprite, True, False)
    walk_left.append(sprite)

jump_right = []
for image in range(1, 9):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Jump ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    jump_right.append(sprite)

jump_left = []
for image in range(1, 9):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Jump ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    sprite = pygame.transform.flip(sprite, True, False)
    jump_left.append(sprite)


class Character(pygame.Rect):
    def __init__(self, sprite_x, sprite_y, sprite_width, sprite_height):
        super().__init__(sprite_x, sprite_y, sprite_width, sprite_height)
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False


character_rect = Character(0, HEIGHT-image_height, image_width, image_height)
current_list = idle_right

floor = pygame.Rect(0, HEIGHT, WIDTH, 1)
left_wall = pygame.Rect(-1, 0, 1, HEIGHT)
right_wall = pygame.Rect(WIDTH, 0, 1, HEIGHT)
ceiling = pygame.Rect(0, -1, WIDTH, 1)

clock = pygame.time.Clock()
running = True
current_sprite = 0
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                current_list = walk_right
                current_sprite = 0
                character_rect.moving_right = True
            elif event.key == pygame.K_a:
                current_list = walk_left
                current_sprite = 0
                character_rect.moving_left = True
            elif event.key == pygame.K_SPACE:
                if current_list in (idle_left, walk_left):
                    current_list = jump_left
                    current_sprite = 0
                elif current_list in (idle_right, walk_right):
                    current_list = jump_right
                    current_sprite = 0
                character_rect.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                current_list = idle_right
                current_sprite = 0
                character_rect.moving_right = False
            elif event.key == pygame.K_a:
                current_list = idle_left
                current_sprite = 0
                character_rect.moving_left = False
    
    if character_rect.moving_up:
        character_rect.move_ip(0, -5)
        if character_rect.colliderect(ceiling):
            character_rect.top = ceiling.bottom
    elif character_rect.moving_down:
        character_rect.move_ip(0, 5)
        if character_rect.colliderect(floor):
            character_rect.bottom = floor.top
    if character_rect.moving_left:
        character_rect.move_ip(-5, 0)
        if character_rect.colliderect(left_wall):
            character_rect.left = left_wall.right
    elif character_rect.moving_right:
        character_rect.move_ip(5, 0)
        if character_rect.colliderect(right_wall):
            character_rect.right = right_wall.left

    
    window.fill(BLACK)
    window.blit(current_list[current_sprite%len(current_list)], (character_rect.x, character_rect.y))

    current_sprite += 1
    
    pygame.display.update()


pygame.quit()