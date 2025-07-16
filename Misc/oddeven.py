from functime import *
import time
from coolprint import *

num = int(input("What number do you want to check? "))


@time_func
def check_num():
    if num % 2 == 0:
        return True
    else:
        return False


x = check_num()

if x == True:
    time.sleep(1)
    print("Your number is even.")
else:
    time.sleep(1)
    print("Your number is odd.")
