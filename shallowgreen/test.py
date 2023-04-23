from chess import *

board = Board()
board = board.move_piece('e2', 'e4')
board = board.move_piece('a7', 'a6')
board = board.move_piece('d1', 'f3')
board = board.move_piece('a6', 'a5')
board = board.move_piece('f3', 'f7')
print("in check?")
print(board.in_check(Board.BLACK))
print("checkmate?")
print(board.check_mate(Board.BLACK))

print(board)
