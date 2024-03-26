import pygame
pygame.init()

FPS = 20
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

img_width = 120
img_height = 120

idle_right = []
idle_left = []

run_right = []
run_left = []

slide_right = []
slide_left = []

for image in range(1, 17):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (img_width, img_height))
    idle_right.append(sprite)
    sprite = pygame.transform.flip(sprite, True, False)
    idle_left.append(sprite)
    
for image in range(1, 12):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Run ({image}).png')
    sprite = pygame.transform.scale(sprite, (img_width, img_height))
    idle_right.append(sprite)
    sprite = pygame.transform.flip(sprite, True, False)
    idle_left.append(sprite)

for image in range(1, 12):
    sprite = pygame.image.load(f'YoungWonks/santasprites/png/Slide ({image}).png')
    sprite = pygame.transform.scale(sprite, (img_width, img_height))
    idle_right.append(sprite)
    sprite = pygame.transform.flip(sprite, True, False)
    idle_left.append(sprite)


class Character(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        
        self.moving_left = False
        self.moving_right = False
        self.sliding_left = False
        self.sliding_right = False


character = Character(WIDTH // 2, HEIGHT // 2, img_width, img_height)


clock = pygame.time.Clock()
running = True
current_list = idle_right
current_sprite = 0
slide_counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         character.moving_right = True
        #         character.moving_left = False
        #         character.sliding_left = False
        #         character.sliding_right = False
        #         current_list = run_right
        #         current_sprite = 0
        #     elif event.key == pygame.K_LEFT:
        #         character.moving_right = False
        #         character.moving_left = True
        #         character.sliding_left = False
        #         character.sliding_right = False
        #         current_list = run_left
        #         current_sprite = 0
        #     elif event.key == pygame.K_SPACE:
        #         if character.moving_right or character.sliding_right:
        #             character.moving_right = False
        #             character.moving_left = False
        #             character.sliding_left = False
        #             character.sliding_right = True
        #             current_list = slide_right
        #         elif character.moving_left or character.sliding_left:
        #             character.moving_right = False
        #             character.moving_left = False
        #             character.sliding_left = True
        #             character.sliding_right = False
        #             current_list = slide_left
                
        #         current_sprite = 0
        #         slide_counter = 0
    
    
    if character.moving_right or character.sliding_right:
        character.move_ip(5, 0)
    elif character.moving_left or character.sliding_left:
        character.move_ip(-5, 0)
    
    # if character.sliding_left or character.sliding_right:
    #     if slide_counter < 15:
    #         slide_counter += 1
    #     elif slide_counter >= 15:
    #         if character.sliding_left:
    #             current_list = idle_left
    #             character.sliding_left = False
    #         else:
    #             current_list = idle_right
    #             character.sliding_right = False
    
    current_sprite += 1
    window.fill(BLACK)
    
    window.blit(current_list[current_sprite%len(current_list)], character)
    
    pygame.display.update()


pygame.quit()
