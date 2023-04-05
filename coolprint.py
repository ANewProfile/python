import random
import time

python_print = print
python_input = input
python_int = int


def print(txt):
    text = str(txt)
    for c in text:
        python_print(c, end="", flush=True)
        time.sleep(random.randint(2, 8)/100)
    python_print()


def input(txt):
    text = str(txt)
    for c in text:
        python_print(c, end="", flush=True)
        time.sleep(random.randint(2, 8)/100)

    python_input("")
    python_print
