import pyautogui as pag
import random
import time

curr_cords = pag.position()
afk_counter = 0
while True:
    if pag.position() == curr_cords:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_cords = pag.position()

    if afk_counter > 5:
        x = random.randint(0, 2250)
        y = random.randint(0, 1500)
        pag.moveTo(x, y, 0.5)
        curr_cords = pag.position()
    print(f'AFK counter is: {afk_counter}')
    time.sleep(2)
