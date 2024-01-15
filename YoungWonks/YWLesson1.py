import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Square:
    def __init__(self, length, color, position, up=False, down=False, left=False, right=False):
        self.length = length
        self.color = color
        self.position = position
        self.up = up
        self.down = down
        self.left = left
        self.right = right
    
    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.length, self.length))
    
    def check_collision_square(self, other):
        if (self.position[1]+self.length > other.position[1] and self.position[1]+self.length < other.position[1]+other.length) and (self.position[0] > other.position[0]):
            self.position[1] = other.position[1]-other.length


x = 524
y = 344

user = Square(32, WHITE, (x, y))
collision1 = Square(50, RED, (492, 538))
collision2 = Square(25, RED, (238, 375))
collision3 = Square(40, RED, (846, 192))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                if event.key == pygame.K_w:
                    user.up = True
                elif event.key == pygame.K_a:
                    user.left = True
                elif event.key == pygame.K_s:
                    user.down = True
                elif event.key == pygame.K_d:
                    user.right = True
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                if event.key == pygame.K_w:
                    user.up = False
                elif event.key == pygame.K_a:
                    user.left = False
                elif event.key == pygame.K_s:
                    user.down = False
                elif event.key == pygame.K_d:
                    user.right = False

    if user.up is True:
        y -= 1
    if user.left is True:
        x -= 1
    if user.right is True:
        x += 1
    if user.down is True:
        y += 1

    if x > 1048:
        x = 1048
    elif x < 0:
        x = 0
    
    if y > 688:
        y = 688
    elif y < 0:
        y = 0

    window.fill(BLACK)
    user.position = (x, y)
    user.draw()

    pygame.display.update()


pygame.quit()