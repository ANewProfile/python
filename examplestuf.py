

from coolprint import *
from functime import *

print("This is cool, right?")


@time_func
def example():
    print("hi, world!")


example()
