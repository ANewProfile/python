import pygame, sys
from pygame import KEYDOWN
import random

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
colors = [cyan, blue, orange, red, yellow, purple, gray]







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
TILE_SIZE = 38
ground = HEIGHT - TILE_SIZE
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('You win!', True, green, black)
text2 = font.render('Don\'t get hit!', True, green, black)
text2rect = text2.get_rect()
text2rect.center = (175, 100)
textRect = text.get_rect()
textRect.center = (540, 120)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Charlie is a OctopusFormer")

# Game States
RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING
# platforms

class platform:
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def collision_check(self, colX, colY, colWidth, colHeight, xSpeed, ySpeed):


        newColX = colX + xSpeed
        newColY = colY + ySpeed
        # Checking Height against top and bottom
        if newColY > self.y and newColY < self.y + self.height or newColY + colHeight > self.y and newColY + colHeight < self.y + self.height:
            if newColX > self.x and newColX < self.x + self.width:
                return True
            if newColX + colWidth > self.x and newColX + colWidth < self.x + self.width:
                return True
        return False


color = green
rcolor = random.choice(colors)
platform1 = platform(100, 10, 100, 400, color)
platform2 = platform(100, 10, 200, 300, color)
platform3 = platform(100, 10, 0, 250, color)
platform4 = platform(100, 10, 200, 150, color)
platform5 = platform(100, 10, 300, 200, color)
platform6 = platform(100, 10, 540, 150, color)
# meteor1 = moving_platform(300, 10, 300, 200, color)








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
                elif event.key == pygame.K_UP and \
                        yPos == ground or \
                         platform1.collision_check(xPos, yPos ,TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True or\
                         platform2.collision_check(xPos, yPos ,TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True or\
                         platform3.collision_check(xPos, yPos ,TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True or\
                         platform4.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True or\
                         platform5.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True or\
                         platform6.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
                    ySpeed = -8

        if platform1.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
            xSpeed = 0
            ySpeed = -7
        if platform2.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
            xSpeed = 0
            ySpeed = -5
        if platform3.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
            xSpeed = 0
            ySpeed = -7

        if platform4.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
            xSpeed = 0
            ySpeed = -7
        if platform5.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
            xSpeed = 0
            ySpeed = -7

        if platform6.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
            xSpeed = 0
            ySpeed = 0
            screen.blit(text, textRect)
            pygame.display.update()
        # if meteor1.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE) == True:
        #     xSpeed = 0
        #     ySpeed = 3
        # if meteor2.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE) == True:
        #     xSpeed = 0
        #     ySpeed = 3
        # if meteor3.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE) == True:
        #     xSpeed = 0
        #     ySpeed = 3
        # if meteor4.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE) == True:
        #     xSpeed = 0
        #     ySpeed = 3
        # if meteor5.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE) == True:
        #     xSpeed = 0
        #     ySpeed = 3
        # if meteor6.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE) == True:
        #     xSpeed = 0
        #     ySpeed = 3

            # if platform7.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE):
            # xSpeed = -10#-10000000000000
            # ySpeed = 0

            if platform1.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
                xSpeed = 0
                ySpeed = 0
            if platform2.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
                xSpeed = 0
                ySpeed = 0
            if platform3.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
                xSpeed = 0
                ySpeed = 0

            if platform4.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
                xSpeed = 0
                ySpeed = 0
            if platform5.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
                xSpeed = 0
                ySpeed = 0

            if platform6.collision_check(xPos, yPos, TILE_SIZE, TILE_SIZE, xSpeed, ySpeed) == True:
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
        # meteor1.draw()
        # meteor2.draw()
        # meteor3.draw()
        # meteor4.draw()
        # meteor5.draw()
        # meteor6.draw()
        # platform7.draw()
        # pygame.draw.rect(screen, purple, (xPos, yPos, TILE_SIZE, TILE_SIZE))
        basketball = pygame.image.load("python test.png")
        screen.blit(basketball, (xPos, yPos))
        pygame.display.update()