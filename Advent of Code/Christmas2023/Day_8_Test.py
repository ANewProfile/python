import sys, re


map = {}
pattern = sys.argv[-1]
f = open('Day_8_Test_Input.txt', 'r')
for line in f.readlines():
    values = re.split('[\s\=\(\)\,]+', line)
    map[values[0]] = [values[1], values[2]]

routes = [0 if c == 'L' else 1 for c in pattern]

def part_one():
    cur = map['AAA']
    for i in range(100_000):
        j = i % len(routes)
        inst = routes[j]
        next_key = cur[inst]
        print(next_key)
        if next_key == 'ZZZ':
            print(i + 1)
            break
        cur = map[next_key]

    print('Done!')

def part_two():
    cur = [node for node, _ in map.items() if node[-1] == 'A']
    print("start", cur)
    for i in range(1000000000000):
        j = i % len(routes)
        inst = routes[j]
        next_keys = [map[key][inst] for key in cur]
        # print("next", next_keys)

        end_chars = [key[-1] for key in next_keys]
        if len(set(end_chars)) == 1:
            print(set(end_chars), next_keys)
            if set(end_chars) == {'Z'}:
                print(i + 1)
                break

        if i % 1000000 == 0:
            print("still going at", i)
        cur = next_keys

    print('Done!')

while True:
    part = int(input('Part: '))
    if part == 1:
        part_one()
        break
    elif part == 2:
        part_two()
        break
    else:
        print('Invalid!')
