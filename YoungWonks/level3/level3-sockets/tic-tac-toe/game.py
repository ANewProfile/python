def check_board(board):
    for row in [[1, 2, 3],
                [4, 5, 6],
                [5, 6, 7],
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
                [1, 5, 9],
                [3, 5, 7]]:
        a, b, c = row
        if board[a] == board[b] == board[c] != None:
            return True

    return False

def move(board, loc, turn):
    new_board = board
    board[loc] = turn
    
    return new_board

def display(board):
    for i in range(1, 4):
        print(board[i], end=' ')
    print()
    for i in range(4, 7):
        print(board[i], end=' ')
    print()
    for i in range(7, 10):
        print(board[i], end=' ')
    print()
    

board = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None
}
