import pygame
pygame.init()

FPS = 10
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
    
    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

circle = Circle(50, WHITE, 930, 360)

image_width = 120
image_height = 120

idle_right = []
for image in range(1, 11):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Idle ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    idle_right.append(sprite)

dying_right = []
for image in range(1, 8):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Dead ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    dying_right.append(sprite)

dead_right = []
for image in range(7, 11):
    sprite = pygame.image.load(f'python/YoungWonks/platformer_game/png/dog/Dead ({image}).png')
    sprite = pygame.transform.scale(sprite, (image_width, image_height))
    dead_right.append(sprite)

image_rect = pygame.Rect(180, 300, image_width, image_height)
current_list = idle_right
current_sprite = 0

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    circle.x -= 10

    if image_rect.collidepoint(circle.x-circle.radius, circle.y):
        current_list = dying_right
        current_sprite = 0
    
    if current_list == dying_right and current_sprite == 8:
        current_list = dead_right
        sprite = 0

    window.fill(BLACK)
    circle.draw()
    window.blit(current_list[current_sprite%len(current_list)], image_rect)
    current_sprite += 1
    pygame.display.update()


pygame.quit()