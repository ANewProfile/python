import re
f = open('Day_1_Input.txt', 'r')
calibrations = [line for line in f.readlines()]

def find_ints(calibration):
    ints = []
    for char in calibration:
        try:
            int(char)
            ints.append(char)
        except:
            continue

    return ints

def find_all_ints(calibration):
    ints = []
    for char in calibration:
        try:
            int(char)
            ints.append(char)
        except:
            ...

    return ints

def part_1():
    print('Running part_1\(\) function...')
    sum = 0
    for calibration in calibrations:
        ints = find_ints(calibration)
        final = int(ints[0] + ints[-1])
        sum += final

    print(f'Sum: {sum}')

def part_2():  # Unfinished
    print('Running part_2\(\) function...')
    sum = 0
    for calibration in calibrations:
        ints = find_all_ints(calibration)
        final = int(ints[0] + ints[-1])
        sum += final

    print(f'Sum: {sum}')

if __name__ == '__main__':
    part = int(input('Part: '))
    if part == 1:
        part_1()
    else:
        part_2()
