import pygame
pygame.init()


FPS = 30
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Circle:
    def __init__(self, radius, color, x, y):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.up = False
        self.left = False
        self.right = False
        self.down = False
    
    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

character = Circle(30, WHITE, 540, 360)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character.up = True
                character.left = False
                character.right = False
                character.down = False
            elif event.key == pygame.K_LEFT:
                character.up = False
                character.left = True
                character.right = False
                character.down = False
            elif event.key == pygame.K_RIGHT:
                character.up = False
                character.left = False
                character.right = True
                character.down = False
            elif event.key == pygame.K_DOWN:
                character.up = False
                character.left = False
                character.right = False
                character.down = True
            elif event.key == pygame.K_SPACE:
                character.up = False
                character.left = False
                character.right = False
                character.down = False

                character.x = 540
                character.y = 360
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                character.up = False
            elif event.key == pygame.K_LEFT:
                character.left = False
            elif event.key == pygame.K_RIGHT:
                character.right = False
            elif event.key == pygame.K_DOWN:
                character.down = False

    if character.up:
        character.y -= 5
    elif character.left:
        character.x -= 5
    elif character.right:
        character.x += 5
    elif character.down:
        character.y += 5

    window.fill(BLACK)
    character.draw()

    pygame.display.update()


pygame.quit()