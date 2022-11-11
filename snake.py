# snake game
import pygame, sys, random
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

TILE_SIZE = 20

# color set up
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (200, 125, 0)


def draw_grid():
    for i in range(25):
        pygame.draw.line(screen, WHITE, (0, i * TILE_SIZE), (639, i * TILE_SIZE))


    for j in range(33):
        pygame.draw.line(screen, WHITE, (j * TILE_SIZE, 0), (j * TILE_SIZE, 479))

def draw_snake(snake_list):
    for pos in snake_list:
        x, y = pos
        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, ORANGE, rect)

def moving_snake(direction):
    global snake_list
    if direction == 'E':
        for i in range(len(snake_list) - 1, 0, -1):
            snake_list[i] = snake_list[i - 1].copy()
        snake_list[0][0] += 1
    elif direction == 'W':
        for i in range(len(snake_list) - 1, 0, -1):
            snake_list[i] = snake_list[i - 1].copy()
        snake_list[0][0] += -1
    elif direction == 'N':
        for i in range(len(snake_list) - 1, 0, -1):
            snake_list[i] = snake_list[i - 1].copy()
        snake_list[0][1] += -1
    elif direction == 'S':
        for i in range(len(snake_list) - 1, 0, -1):
            snake_list[i] = snake_list[i - 1].copy()
        snake_list[0][1] += 1

    draw_snake(snake_list)

def generate_apple(random_pos):
    global screen
    apple_rect = pygame.Rect(random_pos[0] * TILE_SIZE, random_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, RED, apple_rect)

def get_random_pos_for_apple():
    global snake_list
    random_pos = [random.randint(0, 31), random.randint(0, 23)]
    while random_pos in snake_list:
        random_pos = [random.randint(0, 31), random.randint(0, 23)]
    return random_pos






def elongate_snake(moving_dir):
    global snake_list
    if moving_dir == 'N':
        new_head = [snake_list[0][0], snake_list[0][1] - 1]
        snake_list.insert(0, new_head)
    elif moving_dir == 'S':
        new_head = [snake_list[0][0], snake_list[0][1] + 1]
        snake_list.insert(0, new_head)
    elif moving_dir == 'E':
        new_head = [snake_list[0][0] + 1, snake_list[0][1]]
        snake_list.insert(0, new_head)
    else:
        new_head = [snake_list[0][0] - 1, snake_list[0][1]]
        snake_list.insert(0, new_head)


def colide_with_border(snake_list):
    return not (0 <= snake_list[0][0] <= 31 and 0 <= snake_list[0][1] <= 23)

def self_collision(snake_list):
    if snake_list[0] in snake_list[1:]:
        return True
    else:
        return False

def game_over_text():
    global screen
    text_font = pygame.font.SysFont('arial', 50)
    game_over_surf = text_font.render('Game Over!', True, WHITE)
    screen.blit(game_over_surf, (180, 150))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Charlie is a snake')
# snake head start position (15,11)
snake_head = pygame.Rect(15 * TILE_SIZE, 11 * TILE_SIZE, TILE_SIZE, TILE_SIZE)

# create a snake list to contain its head and body coordinates
# at first, there is only the default head position
snake_list = [[15, 11]]

# moving direction of the snake, east by default 'E'
moving_dir = 'E'

game_clock = pygame.time.Clock()

apple_eaten = True

game_over = False

apples = 0

frame_per_second = 4
moves_since_start = 0
keys_since_fed = 0

while True:
    moves_since_start += 1
    # print(snake_list)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            keys_since_fed += 1
            if event.key == K_UP and moving_dir != 'S':
                moving_dir = 'N'
            elif event.key == K_DOWN and moving_dir != 'N':
                moving_dir = 'S'
            elif event.key == K_LEFT and moving_dir != 'E':
                moving_dir = 'W'
            elif event.key == K_RIGHT and moving_dir != 'W':
                moving_dir = 'E'
    screen.fill(BLACK)
    draw_grid()

    if apple_eaten:
        apple_pos = get_random_pos_for_apple()
        apple_eaten = False
        apples += 1
        print(apples)
        keys_since_fed = 0

    generate_apple(apple_pos)

    moving_snake(moving_dir)

    if snake_list[0] == apple_pos:  # if snake ate apple
        apple_eaten = True
        elongate_snake(moving_dir)

    if colide_with_border(snake_list):
        game_over_text()
        game_over = True
    if self_collision(snake_list):
        game_over_text()
        game_over = True

    pygame.display.update()
    if game_over:
        break

    game_clock.tick(frame_per_second+int(moves_since_start/50)+keys_since_fed)
