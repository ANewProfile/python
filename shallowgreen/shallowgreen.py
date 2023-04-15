from chess import *

board = Board()
move = 0

while True:
    if move%2 == 0:
        true_move = 'white'
    else:
        true_move = 'black'
 
    if true_move == 'white':   # white move
        print(board)
        q = [input("Which piece would you like to move? "), input("Where would you like to move it? ")]
        if piece_is_white(board.piece_at(q[0])) is False:
            print("Invalid.")
        else:
            try:
                board = board.move_piece(q[0], q[1])
                move += 1
            except Exception as e:
                print(e)
 
    else:   # black move
        q = board.computer_turn()
        board = board.move_piece(q[0], q[1])
