import pygame
pygame.init()

FPS = 60
WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

sprite = pygame.image.load('YoungWonks/santasprites/png/Idle (1).png')
sprite = pygame.transform.scale(sprite, (120, 120))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Character(pygame.Rect):
    def __init__(self, rect: pygame.Rect):
        super().__init__(rect.x, rect.y, rect.width, rect.height)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height-20)

sprite_rect = Character(pygame.Rect(0, 0, 120, 120))
sprite_rect.hitbox.center = (WIDTH / 2, HEIGHT / 3)

platform = pygame.Rect(0, 0, 360, 20)
platform.center = (WIDTH / 2, HEIGHT * 2/3)

running = True
down = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if platform.colliderect(sprite_rect.hitbox):
        down = False
        sprite_rect.hitbox.bottom = platform.top
    
    if down:
        sprite_rect.hitbox.move_ip(0, 5)

    sprite_rect.center = sprite_rect.hitbox.center


    window.fill(BLACK)

    window.blit(sprite, sprite_rect)
    pygame.draw.rect(window, WHITE, platform)

    pygame.display.update()

pygame.quit()
