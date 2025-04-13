from time import sleep

while True:
    try:
        length = int(input('Input the amount of time you want to wait: '))
        break
    except TypeError:
        print('Please input an integer!')

for i in range(length, 0, -1):
    print(i)
    sleep(1)
