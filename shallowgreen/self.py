from time import sleep
from chess import *
from theo_board_analyzer import *
from look_ahead_player import *

board = Board()
player1 = LookAheadPlayer(TheoBoardAnalyzer, depth=2)
player2 = LookAheadPlayer(TheoBoardAnalyzer, depth=1)
move = 0

while True:
    turn = Board.WHITE if (move % 2 == 0) else Board.BLACK

    if turn == Board.WHITE:  # white move
        print(board)
        try:
            q = player1.computer_turn(board, Board.WHITE)
        except GameOverException as e:
            print(str(e))
            exit()
        print("WHITE %s, board.move_piece('%s','%s')" % (board.piece_locations(), q[0], q[1]))
        print("")
        board = board.move_piece(*q)
        move += 1

        sleep(0.25)

    else:   # black move
        print(board)
        try:
            q = player2.computer_turn(board, Board.BLACK)
        except GameOverException as e:
            print(str(e))
            exit()
        print("BLACK %s, board.move_piece('%s','%s')" % (board.piece_locations(), q[0], q[1]))
        print("")
        board = board.move_piece(*q)
        move += 1

        sleep(0.25)
