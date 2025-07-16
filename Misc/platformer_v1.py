import pygame, sys
from pygame import KEYDOWN

pygame.init()

# Colors
black = (0, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
orange = (255, 100, 10)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
purple = (160, 32, 240)
gray = (190, 190, 190)


class platform:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, green, (self.x, self.y, self.width, self.height))

    def collision_check(self, colX, colY, colWidth, colHeight):

        if colY > self.y and colY < self.y + self.height:                                       #Checking Height against top left(and right)corner
            if colX > self.x and colX < self.x + self.width:                                    #Checking Width against top left corner
                return True
            if colX + colWidth > self.x and colX + colWidth < self.x + self.width:  #Checking Width against top right corner
                return True


        if colY + colHeight> self.y and colY + colHeight< self.y + self.height:
            if colX > self.x and colX < self.x + self.width:
                return True
            if colX + colWidth > self.x and colX + colWidth < self.x + self.width:
                return True
        return False


# Variables for window and tiles
clock = pygame.time.Clock()
FPS = 60
WIDTH = 640
HEIGHT = 480
xPos = 50
xSpeed = 0
yPos = HEIGHT - 50
ySpeed = 0
grav = 0.25
TILE_SIZE = 30
ground = HEIGHT - TILE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Charlie is a PittedFruitFormer")

# Game States
RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING
# platforms
platform1 = platform(100, 10, 100, 400)
platform2 = platform(100, 10, 200, 300)
platform3 = platform(100, 10, 0, 250)
platform4 = platform(100, 10, 200, 150)
platform5 = platform(100, 10, 300, 200)
platform6 = platform(100, 10, 540, 150)
# Game Loop
while True:

    # Loop when player is playing the game
    while game_state == PLAYING:
        # 60 Frames per second
        clock.tick(FPS)
        # xSpeed = 0
        if yPos >= ground:
            ySpeed = 0
        else:
            ySpeed += grav
        # Handle user input / events
        for event in pygame.event.get():

            # When user clicks on the X button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            elif event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xSpeed = 3

                elif event.key == pygame.K_LEFT:
                    xSpeed = -3
                elif event.key == pygame.K_DOWN:
                    ySpeed = 8
                    xSpeed = 0
                elif event.key == pygame.K_UP and yPos == ground:
                    ySpeed = -8


        if platform1.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE) == True:
            xSpeed = 0
            ySpeed = 0
        # Fill screen with black, draw a rectangle, and update display
        xPos += xSpeed
        yPos += ySpeed
        if yPos >= ground:
            yPos = ground
        if xPos >= WIDTH - 30:
            xPos = WIDTH - 30
        if xPos < 0:
            xPos = 0
        screen.fill(black)
        platform1.draw()
        platform2.draw()
        platform3.draw()
        platform4.draw()
        platform5.draw()
        platform6.draw()
        pygame.draw.rect(screen, purple, (xPos, yPos, TILE_SIZE, TILE_SIZE))
        pygame.display.update()