import random
import time

python_print = print


def print(txt):
    text = str(txt)
    for c in text:
        python_print(c, end="", flush=True)
        time.sleep(random.randint(2, 8)/100)
    python_print()
