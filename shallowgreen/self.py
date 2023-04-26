from chess import *
import time

board = Board()
player = Player(TheoBoardAnalyzer)
move = 0

while True:
    turn = Board.WHITE if (move % 2 == 0) else Board.BLACK

    if turn == Board.WHITE:  # white move
        print(board)
        try:
            q = player.computer_turn(board, Board.WHITE)
        except GameOverException as e:
            print(str(e))
            exit()
        print("WHITE board.move_piece('%s','%s')" % (q[0], q[1]))
        print("")
        board = board.move_piece(*q)
        move += 1

        # time.sleep(0.5)

    else:   # black move
        print(board)
        try:
            q = player.computer_turn(board, Board.BLACK)
        except GameOverException as e:
            print(str(e))
            exit()
        print("BLACK board.move_piece('%s','%s')" % (q[0], q[1]))
        print("")
        board = board.move_piece(*q)
        move += 1

        # time.sleep(0.5)
