def find_differences(reading):
    differences = []
    for i in range(len(reading) - 1):
        difference = reading[i+1] - reading[i]
        differences.append(difference)

    return differences

def part_1():
    f = open('Day_9_Input.txt', 'r')
    readings = [[int(num) for num in line.split(' ')] for line in f.readlines()]
    next_values = []
    for reading in readings:
        print('Starting new line!')
        all_zero = False
        old_differences = [reading.copy()]
        while all_zero is False:
            differences = find_differences(old_differences[-1])
            print(differences)
            all_zero = True
            for difference in differences:
                if difference != 0:
                    all_zero = False
                    break
            if all_zero is True:
                next_value = 0
                for differences in old_differences[::-1]:
                    next_value += differences[-1]
                print(f'Next value: {next_value}')
                break
            old_differences.append(differences.copy())
        next_values.append(next_value)
    print(f'Sum of next values: {sum(next_values)}')
    print('Done!')

def part_2():
    f = open('Day_9_Input.txt', 'r')
    readings = [[int(num) for num in line.split(' ')] for line in f.readlines()]
    prev_values = []
    for reading in readings:
        print('Starting new line!')
        all_zero = False
        old_differences = [reading.copy()]
        while all_zero is False:
            differences = find_differences(old_differences[-1])
            print(differences)
            all_zero = True
            for difference in differences:
                if difference != 0:
                    all_zero = False
                    break
            if all_zero is True:
                prev_value = 0
                for differences in old_differences[::-1]:
                    prev_value = differences[0] - prev_value
                print(f'Previous value: {prev_value}')
                break
            old_differences.append(differences.copy())
        prev_values.append(prev_value)
    print(f'Sum of previous values: {sum(prev_values)}')
    print('Done!')

if __name__ == '__main__':
    part = int(input('Part: '))
    if part == 1:
        part_1()
    else:
        part_2()
