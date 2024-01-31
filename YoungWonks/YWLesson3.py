import pygame

pygame.init()

WIDTH = 720
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (
    0,
    0,
    0,
)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

board = {
    (0, 0): None,
    (0, 1): None,
    (0, 2): None,
    (1, 0): None,
    (1, 1): None,
    (1, 2): None,
    (2, 0): None,
    (2, 1): None,
    (2, 2): None,
}

def draw_x(section):
    if section == 1:
        pygame.draw.line(window, RED, (0, 0), (240, 240), width=3)
        pygame.draw.line(window, RED, (240, 0), (0, 240), width=3)
    elif section == 2:
        pygame.draw.line(window, RED, (240, 0), (480, 240), width=3)
        pygame.draw.line(window, RED, (480, 0), (240, 240), width=3)
    elif section == 3:
        pygame.draw.line(window, RED, (480, 0), (720, 240), width=3)
        pygame.draw.line(window, RED, (720, 0), (480, 240), width=3)
    elif section == 4:
        pygame.draw.line(window, RED, (0, 240), (240, 480), width=3)
        pygame.draw.line(window, RED, (240, 240), (0, 480), width=3)
    elif section == 5:
        pygame.draw.line(window, RED, (240, 240), (480, 480), width=3)
        pygame.draw.line(window, RED, (480, 240), (240, 480), width=3)
    elif section == 6:
        pygame.draw.line(window, RED, (480, 240), (720, 480), width=3)
        pygame.draw.line(window, RED, (720, 240), (480, 480), width=3)
    elif section == 7:
        pygame.draw.line(window, RED, (0, 480), (240, 720), width=3)
        pygame.draw.line(window, RED, (240, 480), (0, 720), width=3)
    elif section == 8:
        pygame.draw.line(window, RED, (240, 480), (480, 720), width=3)
        pygame.draw.line(window, RED, (480, 480), (240, 720), width=3)
    else:
        pygame.draw.line(window, RED, (480, 480), (720, 720), width=3)
        pygame.draw.line(window, RED, (720, 480), (480, 720), width=3)


def draw_o(section):
    if section == 1:
        pygame.draw.circle(window, BLUE, (120, 120), 119, width=3)
    elif section == 2:
        pygame.draw.circle(window, BLUE, (360, 120), 119, width=3)
    elif section == 3:
        pygame.draw.circle(window, BLUE, (600, 120), 119, width=3)
    elif section == 4:
        pygame.draw.circle(window, BLUE, (120, 360), 119, width=3)
    elif section == 5:
        pygame.draw.circle(window, BLUE, (360, 360), 119, width=3)
    elif section == 6:
        pygame.draw.circle(window, BLUE, (600, 360), 119, width=3)
    elif section == 7:
        pygame.draw.circle(window, BLUE, (120, 600), 119, width=3)
    elif section == 8:
        pygame.draw.circle(window, BLUE, (360, 600), 119, width=3)
    else:
        pygame.draw.circle(window, BLUE, (600, 600), 119, width=3)


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
            print("MOUSE DOWN")
            mouse_pos = event.pos
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            y_section = mouse_x // 240
            x_section = mouse_y // 240
            if board[(x_section, y_section)] is None:
                board[(x_section, y_section)] = "X" if turn % 2 == 0 else "O"
            else:
                print("INVALID.")
            turn += 1

    window.fill(BLACK)

    # Draw Grid
    pygame.draw.line(window, WHITE, (0, 240), (720, 240))
    pygame.draw.line(window, WHITE, (0, 480), (720, 480))

    pygame.draw.line(window, WHITE, (240, 0), (240, 720))
    pygame.draw.line(window, WHITE, (480, 0), (480, 720))

    for square, value in board.items():
        if value is not None:
            if value is 'X':
                draw_shape(True, square)
            else:
                draw_shape(False, square)

    # print(board)

    pygame.display.update()


pygame.quit()
