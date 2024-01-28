import pygame
pygame.init()

WIDTH = 720
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0, )
RED = (255, 0, 0)
BLUE = (0, 0, 255)

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

def draw_x(section):
    if section == 1:
        pygame.draw.line(window, RED, (0, 0), (0, 0))
        pygame.draw.line(window, RED, (240, 240), (240, 240))
    elif section == 2:
        ...
    elif section == 3:
        ...
    elif section == 4:
        ...
    elif section == 5:
        ...
    elif section == 6:
        ...
    elif section == 7:
        ...
    elif section == 8:
        ...
    else:
        ...

def draw_o(section):
    if section == 1:
        ...
    elif section == 2:
        ...
    elif section == 3:
        ...
    elif section == 4:
        ...
    elif section == 5:
        ...
    elif section == 6:
        ...
    elif section == 7:
        ...
    elif section == 8:
        ...
    else:
        ...

def draw_shape(is_x, section):
    if section == (0, 0):
        if is_x:
            draw_x(1)
        else:
            draw_o(1)
    elif section == (0, 1):
        if is_x:
            draw_x(2)
        else:
            draw_o(2)
    elif section == (0, 2):
        if is_x:
            draw_x(3)
        else:
            draw_o(3)
    elif section == (1, 0):
        if is_x:
            draw_x(4)
        else:
            draw_o(4)
    elif section == (1, 1):
        if is_x:
            draw_x(5)
        else:
            draw_o(5)
    elif section == (1, 2):
        if is_x:
            draw_x(6)
        else:
            draw_o(6)
    elif section == (2, 0):
        if is_x:
            draw_x(7)
        else:
            draw_o(7)
    elif section == (2, 1):
        if is_x:
            draw_x(8)
        else:
            draw_o(8)
    else:
        if is_x:
            draw_x(9)
        else:
            draw_o(9)

running = True
turn = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            x_section = mouse_x // 240
            y_section = mouse_y // 240
            board[x_section][y_section] = 'X' if turn%2 == 0 else 'O'
            turn += 1


    window.fill(BLACK)

    # Draw Grid
    pygame.draw.line(window, WHITE, (0, 240), (720, 240))
    pygame.draw.line(window, WHITE, (0, 480), (720, 480))

    pygame.draw.line(window, WHITE, (240, 0), (240, 720))
    pygame.draw.line(window, WHITE, (480, 0), (480, 720))

    for row in board:
        for column in row:
            if column is not None:
                draw_shape(turn%2==0, (row, column))

    pygame.display.update()


pygame.quit()
