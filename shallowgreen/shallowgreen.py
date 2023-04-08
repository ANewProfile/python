from chess import *

board = Board()
move = 0



while True:
    if move%2 == 0:
        true_move = 'white'
    else:
        true_move = 'black'

    print(board)
    q = [input("Which piece would you like to move? "), input("Where would you like to move it? ")]
    if true_move == 'white':
        # white move
        if board.is_white(q[0]) is False:
            print("Invalid.")
        else:
            board = board.move_piece(q[0], q[1])
            move += 1
    else:
        # black move
        if board.is_white(q[0]) is True:
            print("Invalid.")
        else:
            board = board.move_piece(q[0], q[1])
            move += 1