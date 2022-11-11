import pygame, random, time
pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Brick Breakers")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, 32, 20))

    def update(self):
        key_pressed = pygame.key.get_pressed()
        key_name = pygame.key.name(key_constant)
        if key_pressed[pygame.K_RIGHT]:
            self.x += 5
            print(self.x)

def main():
    myPlayer = Player(200, 350)

    while True:
        myPlayer.update()
        myPlayer.draw()

        # you need the following loop to process all the events, you can put the key press in there
        for event in pygame.event.get():
            pass

        pygame.display.flip()
        screen.fill((000, 000, 000))
        clock.tick(60)

main()





        #HOMEWORK
        #add a function called update that uses arrows to move paddles left or right 5 pixels
        #create a boundary