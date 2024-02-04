import pygame
pygame.init()

WIDTH = 720
HEIGHT = 720
FRAMERATE = 1
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREEN = (144, 238, 144)

STEP_W = WIDTH // 9
STEP_H = HEIGHT // 9

class Player(pygame.Rect):
    def __init__(self, snake, path, right=False, left=False, up=False, down=False):
        self.length = len(snake)
        self.head_x = snake[0][0]
        self.head_y = snake[0][1]
        self.path = path
        self.right = right
        self.left = left
        self.up = up
        self.down = down
    
    def draw(self):
        pygame.draw.rect(window, LIGHT_GREEN, (self.head_x, self.head_y, STEP_W, STEP_H))

class Fruit(pygame.Rect):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, STEP_W, STEP_H)) 

def draw_grid():
    for x in range(0, WIDTH+1, STEP_W):
        pygame.draw.line(window, WHITE, (x, 0), (x, HEIGHT))
    
    for y in range(0, HEIGHT+1, STEP_H):
        pygame.draw.line(window, WHITE, (0, y), (WIDTH, y))

player_x = STEP_W
player_y = int((HEIGHT//2) - (1/2)*(STEP_H))
fruit_x = WIDTH - 2*STEP_W
fruit_y = int((HEIGHT//2) - (1/2)*(STEP_H))

running = True
clock = pygame.time.Clock()
player = Player([[player_x, player_y]], [])
fruit = Fruit(fruit_x, fruit_y)
while running:
    clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.right = False
                player.left = False
                player.up = True
                player.down = False
            elif event.key == pygame.K_DOWN:
                player.right = False
                player.left = False
                player.up = False
                player.down = True
            elif event.key == pygame.K_LEFT:
                print('going left')
                player.right = False
                player.left = True
                player.up = False
                player.down = False
            elif event.key == pygame.K_RIGHT:
                print('going right')
                player.right = True
                player.left = False
                player.up = False
                player.down = False
    
    if player.up is True:
        player_y -= STEP_H
        player.head_y = player_y
    elif player.down is True:
        player_y += STEP_H
        player.head_y = player_y
    elif player.left is True:
        player_x -= STEP_W
        player.head_x = player_x
    else:
        player_x += STEP_W
        player.head_x = player_x
    
    window.fill(BLACK)
    draw_grid()
    player.draw()
    fruit.draw()

    pygame.display.update()

pygame.quit()