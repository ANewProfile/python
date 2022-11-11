import pygame, math
from pygame.locals import *
from tetris_peices import *
pygame.init()




level = 1
score = 0
new_level = 5 * level
drop_clock = 0





black = (0,0,0)
cyan = (0,255,255)
blue = (0,0,255)
orange = (255,100,10)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
purple = (160,32,240)
gray = (190, 190, 190)
pink = (180, 0, 180)
brown = (255, 50, 180)
black = (0, 0, 0)
white = (255, 255, 255)



colors=[black,cyan,blue,orange, yellow, green, purple, red, pink, brown, black, white]



clock = pygame.time.Clock()
FPS = 60
WIDTH = 640
HEIGHT = 480
TILE_SIZE=20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Theo's Tetris")


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score: ' + str(score), True, black, gray)
textRect = text.get_rect()
textRect.center = (380, 20)


def draw_board(board,board_surface):
    for row in range(ROWS):
        for col in range(COLS):
            currentTile = board[row][col]
            tile_x = col * TILE_SIZE
            tile_y = row * TILE_SIZE
            draw_tile(tile_x, tile_y, currentTile, board_surface)



def draw_tile(posX, posY, tile, surface):
    tile_color = colors[tile]
    rect = Rect((posX, posY), (TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(surface,tile_color,rect)
    pygame.draw.rect(surface,gray,rect.inflate(1,1),1)



def draw_play_area(screen_position, screen_surface, board_surface):
    rows_toShow = 20.5
    topY = board_surface.get_height() - rows_toShow * TILE_SIZE
    screen_surface.blit(board_surface,screen_position, Rect((0, topY),(board_surface.get_width(),rows_toShow * TILE_SIZE)))


def draw_Tetrimino(posX, posY, Tetrimino, board_surface):
    topX = posX
    topY = posY
    rows = len(Tetrimino)
    cols = len(Tetrimino[0])




    for row in range(rows):
        for col in range(cols):
            tile = Tetrimino[row][col]
            if tile != 0:
                tileX = (topX + col) * TILE_SIZE
                tileY = (topY + row) * TILE_SIZE
                draw_tile(tileX, tileY, tile, board_surface)


def calculate_drop_time(level):
    return math.floor(math.pow((0.8 - ((level - 1) * 0.007)), level-1) * 60)



def lock(posX, posY, grid, tetrimino):
    top_x, top_y = posX, posY
    tetrimino_height = len(tetrimino)
    tetrimino_width = len(tetrimino[0])
    for y in range(tetrimino_height):
        for x in range(tetrimino_width):
            tile = tetrimino[y][x]
            if tile != 0:
                grid[top_y + y][top_x + x] = tile

def check_and_clear_lines(grid):
    global score
    lines_cleared = 0
    full_lines = []
    for y, line in enumerate(grid):
        if 0 not in line:
            lines_cleared += 1
            score += 1
            full_lines.append(y)

    if lines_cleared > 0:
        for y in full_lines:
            grid.pop(y)
            grid.insert(0, [0 for _ in range(COLS)])




currentDropTime = baseDropTime = calculate_drop_time(level)


locking = False
lock_clock=0
lock_delay=30








ROWS = 40
COLS = 10
board= [[0 for _ in range(COLS)] for _ in range(ROWS)]
board_surface = pygame.Surface((COLS*TILE_SIZE,ROWS*TILE_SIZE))

RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING



active_Tetrimino = Tetrimino()
active_Tetrimino.grid_ref = board
active_Tetrimino.reset()

while True:
    text = font.render('Score: ' + str(score), True, black, gray)
    textRect = text.get_rect()
    textRect.center = (380, 20)

    while game_state == PLAYING:
        clock.tick(FPS)
        text = font.render('Score: ' + str(score), True, black, gray)
        textRect = text.get_rect()
        textRect.center = (380, 20)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_DOWN]:
            active_Tetrimino.move(0, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    active_Tetrimino.move(1, 0)
                elif event.key == pygame.K_LEFT:
                    active_Tetrimino.move(-1, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_x:
                    active_Tetrimino.rotate(1)
                elif event.key == pygame.K_z or event.key == pygame.K_RCTRL:
                    active_Tetrimino.rotate(-1)

        drop_clock += 1
        if drop_clock >= currentDropTime:
            move = active_Tetrimino.move(0, 1)


            if not move:
                # we hit something!
                if not locking:
                    locking = True
                    lock_clock = 0
            else:
                # no longer locking
                locking = False
            drop_clock = 0

        if locking:
            lock_clock += 1
            if lock_clock >= lock_delay:
                lock(active_Tetrimino.x, active_Tetrimino.y, board,
                     peices[active_Tetrimino.type][active_Tetrimino.rotation])
                drop_clock = baseDropTime
                active_Tetrimino.reset()
                lock_clock = 0
                locking = False
                check_and_clear_lines(board)

        screen.fill(gray)
        draw_board(board, board_surface)
        draw_Tetrimino(active_Tetrimino.x, active_Tetrimino.y, peices[active_Tetrimino.type][active_Tetrimino.rotation],
        board_surface)
        draw_play_area((10, 10), screen, board_surface)
        screen.blit(text, textRect)
        pygame.display.update()