from chess import *

board = Board()

board = board.move_piece('a2','a3')
board = board.move_piece('b8','a6')
board = board.move_piece('e2','e3')
board = board.move_piece('a6','b8')
board = board.move_piece('d1','f3')
board = board.move_piece('g8','h6')

print(board)
move = board.computer_turn(Board.WHITE)
print(move)
