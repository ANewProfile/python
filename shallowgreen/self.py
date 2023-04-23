from chess import *
import time

board = Board()
move = 0

while True:
    turn = Board.WHITE if (move % 2 == 0) else Board.BLACK

    if turn == Board.WHITE:  # white move
        print(board)
        q = board.computer_turn(Board.WHITE)
        print("WHITE wants to move", q)
        print("")
        board = board.move_piece(*q)
        move += 1

        # time.sleep(0.5)

    else:   # black move
        print(board)
        q = board.computer_turn(Board.BLACK)
        print("BLACK wants to move", q)
        print("")
        board = board.move_piece(*q)
        move += 1

        # time.sleep(0.5)
