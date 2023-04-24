from chess import *

board = Board()
board = board.move_piece('d2','d4')
board = board.move_piece('b8','c6')
board = board.move_piece('c1','g5')
board = board.move_piece('d7','d6')
board = board.move_piece('d4','d5')
board = board.move_piece('c6','b4')
board = board.move_piece('d1','d4')
board = board.move_piece('b4','c2')

print(board)
move = board.computer_turn(Board.WHITE)
print(move)
