from math import sqrt

def transform(input: str):
    n = input.split()[0]
    p = int(input.split()[1])
    
    left_digits = []
    right_digits = []
    
    primes = []
    for i in range(2, round(sqrt(int(n[-p]))+1)):
        if int(n[-p])%i == 0:
            primes.append(i)
        continue
    
    pth_digit = str(len(primes))
    
    for i in range(0, len(n)-p-1):
        sum_digits = int(n[i]) + int(n[-p])
        left_digits.append(str(sum_digits))
        continue
    
    for i in range(len(n)-p, len(n)):
        if i >= len(n):
            break
        
        right_digits.append(str(abs(int(n[i]) - int(n[-p]))))

    return "".join(left_digits) + pth_digit + "".join(right_digits)

print(transform('102438 3'))
print(transform('4329 1'))
print(transform('6710 2'))
print(transform('16807 1'))
print(transform('60098065452 7'))
    