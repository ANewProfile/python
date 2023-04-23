from chess import *

board = Board()
move = 0

while True:
    turn = Board.WHITE if (move % 2 == 0) else Board.BLACK

    if turn == Board.WHITE:  # white move
        print("")
        print(board)
        q = board.computer_turn(Board.WHITE)
        print("WHITE wants to move", q)
        board = board.move_piece(*q)
        move += 1

    else:   # black move
        print("")
        print(board)
        q = board.computer_turn(Board.BLACK)
        print("BLACK wants to move", q)
        board = board.move_piece(*q)
        move += 1
