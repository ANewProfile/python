from chess import *

board = Board()
move = 0

while True:
    turn = Board.WHITE if (move % 2 == 0) else Board.BLACK

    if turn == Board.WHITE:  # white move
        print(board)
        q = [input("Which piece would you like to move? "),
             input("Where would you like to move it? ")]
        if piece_color(board.piece_at(q[0])) != Board.WHITE:
            print("Please move a white piece")
        else:
            try:
                board = board.move_piece(q[0], q[1])
                move += 1
            except Exception as e:
                print(e)

    else:   # black move
        q = board.computer_turn(Board.BLACK)
        print("computer wants to move", q)
        board = board.move_piece(*q)
        print("computer move:", *q)
        move += 1
