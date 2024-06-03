import pyautogui as pag
import random
import time

# curr_cords = pag.position()
# afk_counter = 0
# while True:
#     if pag.position() == curr_cords:
#         afk_counter += 1
#     else:
#         afk_counter = 0
#         curr_cords = pag.position()

#     if afk_counter > 5:
#         x = random.randint(0, 1080)
#         y = random.randint(0, 720)
#         pag.moveTo(x, y, 0.5)
#         curr_cords = pag.position()
#     print(f'AFK counter is: {afk_counter}')
#     time.sleep(2)

def press_spacebar():
    pag.press(' ')
    
# time.sleep(10)
# pag.displayMousePosition()

time.sleep(3)
running = True
while running:
    screen = pag.screenshot()
    pixel = screen.getpixel(pag.position())
    print(pixel)
    if (pixel[:-1]) == (182, 182, 182):
        press_spacebar()
    else:
        print('Not white')
