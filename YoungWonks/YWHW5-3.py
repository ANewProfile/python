import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pygame.draw.circle(window, BLUE, (300, 540), 50)
    pygame.draw.circle(window, BLUE, (600, 540), 50)
    pygame.draw.line(window, BLUE, (300, 490), (350, 440), width=20)
    pygame.draw.line(window, BLUE, (600, 490), (550, 440), width=20)
    pygame.draw.line(window, BLUE, (350, 440), (550, 440), width=20)
    pygame.draw.line(window, BLUE, (380, 440), (380, 380), width=20)
    pygame.draw.rect(window, BLUE, (350, 360, 75, 20))
    pygame.draw.line(window, BLUE, (500, 440), (550, 340), width=20)
    pygame.draw.line(window, BLUE, (510, 290), (590, 390), width=20)
    pygame.draw.line(window, BLUE, (460, 390), (510, 490), width=20)  #
    pygame.draw.line(window, BLUE, (440, 390), (480, 390), width=15)
    pygame.draw.line(window, BLUE, (490, 490), (530, 490), width=15)


    pygame.display.update()


pygame.quit()