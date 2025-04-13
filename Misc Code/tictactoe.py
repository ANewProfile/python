import termcolor

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check(board):
  for row in [[0, 3, 6], 
              [1, 4, 7], 
              [2, 5, 8], 
              [0, 1, 2], 
              [3, 4, 5], 
              [6, 7, 8],
              [0, 4, 8], 
              [2, 4, 6]]:
    a, b, c = row
    if board[a] == board[b] == board[c]:
      return True

  return False


def display(board):
  print(board[:3])
  print(board[3:6])
  print(board[6:])
  print("")


move = 'X'
count = 1

while True:
  if count % 2 == 0:
    move = 'X'
  else:
    move = 'O'

  display(board)
  if move == 'O':
    a = int(input(termcolor.colored(move + " move ", "green", attrs=["underline"]))) - 1
  else:
    a = int(input(termcolor.colored(move + " move ", "red", attrs=["underline"]))) - 1


  if board[a] != a + 1:
    continue
  if move == 'O':
    board[a] = move
  else:
    board[a] = move
  print('')

  if check(board):
    print(termcolor.colored("WIN", "yellow", attrs=["bold"]))
    display(board)
    break

  count += 1
  if count > 9:
    print(termcolor.colored('TIE', "magenta", attrs=["bold"]))
    display(board)
    break