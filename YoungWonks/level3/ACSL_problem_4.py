import time
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

path = input[40:]
input = input[:40]

row = 0
for i in range (0, 40):
    board[row].append(input[i])
    row += 1
    row = row % 8
    

print(board)
print(path)
