import time

def get_value(board, loc):
    value = board[loc//10 - 1][loc%10 - 1]
    return value

board = [[],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
]
path = []


input = input("enter the input: ")
input = input.split()

path = [int(location) for location in input[40:]]
input = [int(value) for value in input[:40]]

row = 0
for i in range (0, 40):
    board[row].append(input[i])
    if len(board[row]) == 5:
        row += 1

path_values = [get_value(board, location) for location in path]
path_sum = sum(path_values)
exponent = 0
while True:
    if 2**exponent >= path_sum:
        replace_with = 2**exponent
        break
    else:
        exponent += 1

board[path[-1]//10 - 1][path[-1]%10 - 1] = replace_with
path = path[:-1]

for location in path:
    board[location//10 - 1][location%10 - 1] = None

current_replacement = 0
while True:
    changed = False
    for row in range(0, 7):  # for each row index in the board
        for column in range(0, 4):  # for each column index in the board
            if not board[row][column]:  # value is None
                if row != 0:  # value not in top row
                    changed = True
                    for gravity in range(row-1, -1, -1):  # move above rows down
                        board[gravity+1][column] = board[gravity][column]
                    board[0][column] = None
                else:  # value is in top row
                    changed = True
                    board[row][column] = 2 ** (8 - current_replacement)
                    current_replacement += 1
                    current_replacement = current_replacement % 8
    
    if not changed:
        break

print(board)

# print(board)
# print(path)
