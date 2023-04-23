from chess import *

# does not blunder queen
b = Board()
b = b.move_piece('d2', 'd4')
b = b.move_piece('g8', 'f6')
b = b.move_piece('e2', 'e4')
b = b.move_piece('b8', 'c6')
print(b)
# moving d1h5 would make queen vulnerable to a knight
move = b.computer_turn(Board.WHITE)
assert move[0] != "d1" or move[1] != "h5"
print("next move", move)
