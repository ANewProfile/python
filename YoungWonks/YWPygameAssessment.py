import pygame
pygame.init()

FPS = 30
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

img_w = 120
img_h = 120

idle_left = []
idle_right = []

run_left = []
run_right = []

for i in range(1, 17):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Idle ({i}).png')
    sprite = pygame.transform.scale(sprite, (img_w, img_h))
    idle_right.append(sprite)
    sprite = pygame.transform.flip(sprite, True, False)
    idle_left.append(sprite)

for i in range(1, 12):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Run ({i}).png')
    sprite = pygame.transform.scale(sprite, (img_w, img_h))
    run_right.append(sprite)
    sprite = pygame.transform.flip(sprite, True, False)
    run_left.append(sprite)

def make_text(msg, color, size):
    fontobj = pygame.font.SysFont('freesans', size)
    return fontobj.render(msg, False, color)

idle_left_text = make_text('Idle (Left)', WHITE, 50)
run_left_text = make_text('Run (Left)', WHITE, 50)
idle_right_text = make_text('Idle (Right)', WHITE, 50)
run_right_text = make_text('Run (Right)', WHITE, 50)

sprite_rect = pygame.Rect(0, 0, img_w, img_h)
sprite_rect.center = (WIDTH//2, HEIGHT//2)

current_list = idle_right
current_sprite = 0

move_right = False
move_left = False

current_text = idle_right_text
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
                move_left = False
                current_list = run_right
                current_sprite = 0
            elif event.key == pygame.K_LEFT:
                move_left = True
                move_right = False
                current_list = run_left
                current_sprite = 0
        elif event.type == pygame.KEYUP:
            move_right = False
            move_left = False
            if event.key == pygame.K_RIGHT:
                current_list = idle_right
                current_sprite = 0
            elif event.key == pygame.K_LEFT:
                current_list = idle_left
                current_sprite = 0
    
    if move_right:
        current_text = run_right_text
        sprite_rect.move_ip(5, 0)
    elif move_left:
        current_text = run_left_text
        sprite_rect.move_ip(-5, 0)
    elif idle_right:
        current_text = idle_right_text
    elif idle_left:
        current_text = idle_left_text
    
    window.fill(BLACK)
    
    window.blit(current_text, (30, 30))
    window.blit(current_list[current_sprite%len(current_list)], sprite_rect)
    
    pygame.display.update()
    
    current_sprite += 1


pygame.quit()