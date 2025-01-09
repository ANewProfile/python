import random
import time

python_print = print
python_input = input


def print(txt, speed=(random.randint(2, 8)/100)):
    text = str(txt)
    for c in text:
        python_print(c, end="", flush=True)
        time.sleep(speed)
    python_print()


def input(txt, speed=(random.randint(2, 8)/100)):
    text = str(txt)
    for c in text:
        python_print(c, end="", flush=True)
        time.sleep(speed)

    go = python_input("")
    python_print()
    return go
