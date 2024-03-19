import pygame
pygame.init()

FPS = 30
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREEN = (144, 238, 144)
RED = (255, 0, 0)
BLUE = (173, 216, 230)


image_width = 60
image_height = 60

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

walk_right = []
for image in range(1, 11):
    sprite = pygame.image.load(f'YoungWonks/platformer_game/png/dog/Walk ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    walk_right.append(sprite)

walk_left = []
for image in range(1, 11):
    sprite = pygame.image.load(f'YoungWonks/platformer_game/png/dog/Walk ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    sprite = pygame.transform.flip(sprite, True, False)
    walk_left.append(sprite)

jump_right = []
for image in range(1, 9):
    sprite = pygame.image.load(f'YoungWonks/platformer_game/png/dog/Jump ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    jump_right.append(sprite)

jump_left = []
for image in range(1, 9):
    sprite = pygame.image.load(f'YoungWonks/platformer_game/png/dog/Jump ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    sprite = pygame.transform.flip(sprite, True, False)
    jump_left.append(sprite)

background = pygame.image.load(f'YoungWonks/platformer_game/deserttileset/png/BG.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


middle_grass_image = pygame.image.load(f'YoungWonks/platformer_game/deserttileset/png/Tile/2.png')
middle_grass_image = pygame.transform.scale(middle_grass_image, (20, 20))
left_grass_image = pygame.image.load(f'YoungWonks/platformer_game/deserttileset/png/Tile/1.png')
left_grass_image = pygame.transform.scale(left_grass_image, (20, 20))
right_grass_image = pygame.image.load(f'YoungWonks/platformer_game/deserttileset/png/Tile/3.png')
right_grass_image = pygame.transform.scale(right_grass_image, (20, 20))


class Character(pygame.Rect):
    def __init__(self, sprite_x, sprite_y, sprite_width, sprite_height):
        super().__init__(sprite_x, sprite_y, sprite_width, sprite_height)
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width-(image_width/2), self.height)


level_one = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


board = level_one

def convert_index_to_coords(i, j):  # i = row, j = column
    return (j*20, i*20)

collision_platforms = []
middle_grass_platforms = []
left_grass_platforms = []
right_grass_platforms = []
for row in range(len(board)):
    for column in range(len(board[row])):
        if board[row][column] == 1:
            coords = convert_index_to_coords(row, column)
            platform = pygame.Rect(coords[0], coords[1], 20, 20)
            collision_platforms.append(platform)
            if board[row][column+1] == 1 and board[row][column-1] != 1:
                left_grass_platforms.append(platform)
            elif board[row][column-1] == 1 and board[row][column+1] != 1:
                right_grass_platforms.append(platform)
            else:
                middle_grass_platforms.append(platform)


with open('YoungWonks/platformer_game/save.txt', 'r') as save_file:
    line = save_file.readline()
    # print(line)
    if line:
        data = line.split(' ')
        # print(data)
        for num in range(len(data)):
            # print(data[num])
            data[num] = int(data[num])
        character_rect = Character(data[0], data[1], data[2], data[3])
    else:
        character_rect = Character(0, HEIGHT-image_height, image_width, image_height)

current_list = idle_right

# if platform.collide_point(hitbox.left, hitbox.bottom+1) or platform.collide_point(hitbox.right, hitbox.bottom+1):
#    DO NOT JUMP

bg_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

floor = pygame.Rect(0, HEIGHT, WIDTH, 1)
left_wall = pygame.Rect(-1, 0, 1, HEIGHT)
right_wall = pygame.Rect(WIDTH, 0, 1, HEIGHT)
ceiling = pygame.Rect(0, -1, WIDTH, 1)

collision_platforms.append(floor)
collision_platforms.append(left_wall)
collision_platforms.append(right_wall)
collision_platforms.append(ceiling)

title_rect = pygame.Rect(0, 0, WIDTH, 100)
start_rect = pygame.Rect(500, 100, WIDTH/4, 80)
quit_rect = pygame.Rect(500, 150, WIDTH/4, 80)
def display_start_screen():
    pygame.draw.rect(window, LIGHT_GREEN, title_rect)
    pygame.draw.rect(window, RED, start_rect)
    pygame.draw.rect(window, BLUE, quit_rect)

running = True
clock = pygame.time.Clock()
current_sprite = 0
up_counter = 0
jumped = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('YoungWonks/platformer_game/save.txt', 'w') as save_file:
                save_file.write(f'{character_rect.x} {character_rect.y} {character_rect.width} {character_rect.height}')
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
            elif event.key == pygame.K_SPACE and not jumped:
                if not character_rect.moving_up:
                    if current_list in (idle_left, walk_left):
                        current_list = jump_left
                    elif current_list in (idle_right, walk_right):
                        current_list = jump_right
                    current_sprite = 0
                    up_counter = 0
                    character_rect.moving_up = True
                jumped = True
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
        character_rect.hitbox.move_ip(0, -5)
        if character_rect.hitbox.colliderect(ceiling):
            character_rect.hitbox.top = ceiling.bottom
        for platform in collision_platforms:
            if character_rect.hitbox.colliderect(platform):
                character_rect.hitbox.top = platform.bottom
        up_counter += 1
    elif character_rect.moving_down:
        last_y = character_rect.hitbox.top
        character_rect.hitbox.move_ip(0, 5)
        if character_rect.hitbox.colliderect(floor):
            character_rect.hitbox.bottom = floor.top
            jumped = False
            character_rect.moving_down = False
        for platform in collision_platforms:
            if character_rect.hitbox.colliderect(platform):
                character_rect.hitbox.bottom = platform.top
                jumped = False

        if last_y != character_rect.hitbox.top:
            # print(last_y, character_rect.hitbox.top)
            jumped = True

    if character_rect.moving_left:
        character_rect.hitbox.move_ip(-5, 0)
        if character_rect.hitbox.colliderect(left_wall):
            character_rect.hitbox.left = left_wall.right
        for platform in collision_platforms:
            if character_rect.hitbox.colliderect(platform):
                character_rect.hitbox.left = platform.right
    elif character_rect.moving_right:
        character_rect.hitbox.move_ip(5, 0)
        if character_rect.hitbox.colliderect(right_wall):
            character_rect.hitbox.right = right_wall.left
        for platform in collision_platforms:
            if character_rect.hitbox.colliderect(platform):
                character_rect.hitbox.right = platform.left
    
    

    character_rect.center = character_rect.hitbox.center

    if up_counter >= (FPS * (3/4)):
        character_rect.moving_up = False
        character_rect.moving_down = True
        if current_list == jump_right:
            current_list = idle_right
        elif current_list == jump_left:
            current_list = idle_left
    
    if not character_rect.moving_up and not character_rect.moving_left and not character_rect.moving_right:
        character_rect.moving_down = True


    window.fill(BLACK)
    window.blit(background, bg_rect)

    # for platform in middle_grass_platforms:
    #     window.blit(middle_grass_image, platform)

    # for platform in left_grass_platforms:
    #     window.blit(left_grass_image, platform)

    # for platform in right_grass_platforms:
    #     window.blit(right_grass_image, platform)

    # window.blit(current_list[current_sprite%len(current_list)], character_rect)

    # # if jumped and the ground below the character is not air:
    # #     jumped = False

    # current_sprite += 1
    # if current_list in (jump_left, jump_right) and current_sprite >= len(current_list):
    #     current_sprite -= 1

    display_start_screen()
    
    pygame.display.update()


pygame.quit()