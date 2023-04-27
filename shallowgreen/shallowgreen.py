from chess import *
from theo_board_analyzer import *
from look_ahead_player import *

board = Board()
player = LookAheadPlayer(TheoBoardAnalyzer, depth=2)
move = 0

while True:
    turn = Board.WHITE if (move % 2 == 0) else Board.BLACK

    if turn == Board.WHITE:  # white move
        print(board)
        q = [input("Which piece would you like to move? "),
             input("Where would you like to move it? ")]
        if piece_color(board.piece_at(q[0])) != Board.WHITE:
            print("Please move a white piece.")
        else:
            try:
                board = board.move_piece(q[0], q[1])
                move += 1
            except InvalidMoveException as e:
                print(e)

    else:   # black move
        try:
            q = player.computer_turn(board, Board.BLACK)
        except GameOverException as e:
            print(str(e))
            exit()
        board = board.move_piece(*q)
        print("COMPUTER MOVE:", *q)
        move += 1
