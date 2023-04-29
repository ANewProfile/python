from chess import *
from dad_board_analyzer import *
from player import *

board = Board()
player = LookAheadPlayer(DadBoardAnalyzer, depth=2)
move = 0

while True:
    turn = Board.WHITE if (move % 2 == 0) else Board.BLACK

    if turn == Board.WHITE:  # white move
        print(board)
        q = [input("Which piece would you like to move? "),
             input("Where would you like to move it? ")]
        if len(q[0]) != 2 or len(q[1]) != 2 or \
           piece_color(board.piece_at(q[0])) != Board.WHITE or \
           board.piece_at(q[1]) is not None:
            print("Please move a white piece to an empty space.")
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
        print(board.piece_locations())
        board = board.move_piece(*q)
        print("COMPUTER MOVE:", *q)
        move += 1
