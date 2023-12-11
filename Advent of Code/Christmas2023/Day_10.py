with open('Day_10_Test_Input.txt', 'r') as f:
    rows = [row[:-1] for row in f.readlines()]

for row in rows:
    if row.find('S') != -1:
        s_index = (rows.index(row), row.find('S'))

def find_loop(rows, current_pos, start_pos=None, last_pos=None, failed=[]):
    local_s = s_index
    cur_position = current_pos[0], current_pos[1]
    # print(cur_position)
    print(failed)
    if cur_position == 'S' and cur_position != local_s:
        return start_pos, last_pos
    elif cur_position == 'S' and cur_position == local_s:
        if (cur_position[0]-1, cur_position[1]) not in failed:
            find_loop(rows, (cur_position[0]-1, cur_position[1]), (cur_position[0]-1, cur_position[1]), cur_position, failed)
        elif (cur_position[0], cur_position[1]+1) not in failed:
            find_loop(rows, (cur_position[0], cur_position[1]+1), (cur_position[0], cur_position[1]+1), cur_position, failed)
        elif (cur_position[0]+1, cur_position[1]) not in failed:
            find_loop(rows, (cur_position[0]+1, cur_position[1]), (cur_position[0]+1, cur_position[1]), cur_position, failed)
        else:
            find_loop(rows, (cur_position[0], cur_position[1]-1), (cur_position[0], cur_position[1]-1), cur_position, failed)
    else:
        if cur_position == '|':
            if last_pos == (cur_position[0]+1, cur_position[1]):
                find_loop(rows, (cur_position[0]-1, cur_position[1]), start_pos, cur_position, failed)
            else:
                find_loop(rows, (cur_position[0]+1, cur_position[1]), start_pos, cur_position, failed)
        elif cur_position == '-':
            if last_pos == (cur_position[0], cur_position[1]+1):
                find_loop(rows, (cur_position[0], cur_position[1]-1), start_pos, cur_position, failed)
            else:
                find_loop(rows, (cur_position[0], cur_position[1]+1), start_pos, cur_position, failed)
        elif cur_position == 'L':
            if last_pos == (cur_position[0]+1, cur_position[1]):
                find_loop(rows, (cur_position[0], cur_position[1]+1), start_pos, cur_position, failed)
            else:
                find_loop(rows, (cur_position[0]-1, cur_posiiton[1]), start_pos, cur_position, failed)
        elif cur_position == 'J':
            if last_pos == (cur_position[0]+1, cur_position[1]):
                find_loop(rows, (cur_position[0], cur_position[1]-1), start_pos, cur_position, failed)
            else:
                find_loop(rows, (cur_position[0]-1, cur_position[1]), start_pos, cur_position, failed)
        elif cur_position == '7':
            if last_pos == (cur_position[0], cur_position[1]-1):
                find_loop(rows, (cur_position[0]+1, cur_position[1]), start_pos, cur_position, failed)
            else:
                find_loop(rows, (cur_position[0], cur_position[1]-1), start_pos, cur_position, failed)
        elif cur_position == 'F':
            if last_pos == (cur_position[0], cur_position[1]+1):
                find_loop(rows, (cur_position[0]+1, cur_position[1]), start_pos, cur_position, failed)
            else:
                find_loop(rows, (cur_position[0], cur_position[1]+1), start_pos, cur_position, failed)
        else:
            find_loop(rows, local_s, failed=failed.append(start_pos))

def part_1():
    local_s = s_index
    # print(local_s)
    loop = find_loop(rows, local_s)
    print(loop)

def part_2():
    ...

if __name__ == '__main__':
    part = int(input('Part: '))
    if part == 1:
        part_1()
    else:
        part_2()
