from threading import Thread
from math import sqrt, floor


def find_factors(num):
    factors = []
    
    if num < 0:
        print('Number is negative')
    
    if num == 2:
        factors.append(1)
        factors.append(2)
    elif num == 1:
        factors.append(1)
    elif num == 0:
        factors.append(0)
    else:
        for i in range(1, floor(sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num/i)
    
    print(factors)
    
for i in range(1_000_000, 10_000_000):
    thread = Thread(target=find_factors, args=(i,))
    thread.start()
