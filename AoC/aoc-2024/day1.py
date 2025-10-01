def parse_input(input):
    left_list = []
    right_list = []
    i = 0
    for id in input.split():
        if i % 2 == 0:
            left_list.append(int(id))
        else:
            right_list.append(int(id))

        i += 1

    return left_list, right_list

def main():
    with open('day1input.txt', 'r') as input:
        left_list, right_list = parse_input(input.read())

    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    total = 0

    for i in range(0, len(sorted_left)):
        total += abs(sorted_left[i] - sorted_right[i])

    return total

if __name__ == '__main__':
    response = main()
    print(response)

