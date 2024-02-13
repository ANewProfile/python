import pygame
import random
from time import sleep
pygame.init()

WIDTH = 720
HEIGHT = 720
FRAMERATE = 5
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREEN = (144, 238, 144)
BLUE = (173, 216, 230)

GRID_SIZE = 9
STEP_W = WIDTH // GRID_SIZE
STEP_H = HEIGHT // GRID_SIZE


class Player(pygame.Rect):
    def __init__(self, snake, right=False, left=False, up=False, down=False):
        self.length = len(snake)
        self.head_x = snake[0][0]
        self.head_y = snake[0][1]
        pygame.Rect.__init__(self, self.head_x, self.head_y, STEP_W, STEP_H)
        self.snake = snake
        self.go_right = right
        self.go_left = left
        self.up = up
        self.down = down
    
    def move(self, x, y):
        # 1. Second item becomes the value of first item
        # 2. Third item becomes the value of fourth item
        # 3. Repeat until you make last item the value of second to last item
        # 4. Set first item to where you're going next

        # self.move_ip(x, y)
        # for i in range(1, len(self.snake)):
        #     self.snake[i] = self.snake[i-1]
        # self.snake[0] = [self.snake[0][0]+x, self.snake[0][1]+y]

        self.move_ip(x, y)
        if len(self.snake) > 1:
            self.snake = self.snake[:-1]
            self.snake.insert(0, [self.snake[0][0]+x, self.snake[0][1]+y])
        else:
            self.snake[0] = [self.snake[0][0]+x, self.snake[0][1]+y]
    
    def draw(self):
        for square in self.snake[1:]:
            pygame.draw.rect(window, LIGHT_GREEN, (square[0], square[1], STEP_W, STEP_H))
        pygame.draw.rect(window, BLUE, (self.snake[0][0], self.snake[0][1], STEP_W, STEP_H))
    
    def elongate(self):
        if self.up:
            self.snake.append([self.snake[-1][0], self.snake[-1][1]+STEP_W])
        elif self.down:
            self.snake.append([self.snake[-1][0], self.snake[-1][1]-STEP_W])
        elif self.right:
            self.snake.append([self.snake[-1][0]+STEP_H, self.snake[-1][1]])
        else:
            self.snake.append([self.snake[-1][0]-STEP_H, self.snake[-1][1]])

class Fruit(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, STEP_W, STEP_H)

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, STEP_W, STEP_H)) 

def draw_grid():
    for x in range(0, WIDTH+1, STEP_W):
        pygame.draw.line(window, WHITE, (x, 0), (x, HEIGHT))
    
    for y in range(0, HEIGHT+1, STEP_H):
        pygame.draw.line(window, WHITE, (0, y), (WIDTH, y))

if GRID_SIZE % 2 == 1:
    player_x = STEP_W
    player_y = int((HEIGHT//2) - (1/2)*(STEP_H))
    fruit_x = WIDTH - 2*STEP_W
    fruit_y = int((HEIGHT//2) - (1/2)*(STEP_H))
else:
    player_x = STEP_W
    player_y = HEIGHT // 2
    fruit_x = WIDTH - 2*STEP_W
    fruit_y = HEIGHT // 2

score = 0
already_increased_size = False

running = True
clock = pygame.time.Clock()
player = Player([[player_x, player_y]], True)
fruit = Fruit(fruit_x, fruit_y)
while running:
    clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.down is not True:
                    player.go_right = False
                    player.go_left = False
                    player.up = True
                    player.down = False
            elif event.key == pygame.K_DOWN:
                if player.up is not True:
                    player.go_right = False
                    player.go_left = False
                    player.up = False
                    player.down = True
            elif event.key == pygame.K_LEFT:
                if player.go_right is not True:
                    player.go_right = False
                    player.go_left = True
                    player.up = False
                    player.down = False
            elif event.key == pygame.K_RIGHT:
                if player.go_left is not True:
                    player.go_right = True
                    player.go_left = False
                    player.up = False
                    player.down = False

    if player.up is True:
        player.move(0, -STEP_H)
    elif player.down is True:
        player.move(0, STEP_H)
    elif player.go_left is True:
        player.move(-STEP_W, 0)
    else:
        player.move(STEP_W, 0)
    
    if player.colliderect(fruit):
        fruit.update(random.randint(0, GRID_SIZE-1)*STEP_W, random.randint(0, GRID_SIZE-1)*STEP_H, STEP_W, STEP_H)
        player.elongate()
        score += 1
    
    for part in player.snake[1:]:
        temp_rect = pygame.Rect(part[0], part[1], STEP_W, STEP_H)
        if player.colliderect(temp_rect):
            print(f'Game over! Your score was: {score}')
            running = False
    temp_rect = None

    if player.snake[0][0] > WIDTH or player.snake[0][1] > HEIGHT or player.snake[0][0] < 0 or player.snake[0][1] < 0:
        print(f'Game over! Your score was: {score}')
        running = False

    if score % 10 == 0 and score > 0 and not already_increased_size:
        GRID_SIZE += 1
        already_increased_size = True
        height_difference = HEIGHT // GRID_SIZE - (HEIGHT // (GRID_SIZE - 1))
        width_difference = WIDTH // GRID_SIZE - (WIDTH // (GRID_SIZE - 1))
        player.snake = [[part[0]-width_difference, part[1]-height_difference] for part in player.snake]
    
    if score % 10 != 0 and already_increased_size:
        already_increased_size = False
    
    STEP_W = WIDTH // GRID_SIZE
    STEP_H = HEIGHT // GRID_SIZE
    
    window.fill(BLACK)
    draw_grid()
    fruit.draw()
    player.draw()

    pygame.display.update()

pygame.quit()