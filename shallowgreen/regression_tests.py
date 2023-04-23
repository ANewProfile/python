from chess import *

# pawn movements
b = Board()
nb = b.move_piece('e2', 'e4')
assert b.location_of("p5") == "e2"
assert nb.location_of("p5") == "e4"
nb = b.move_piece('a7', 'a6')
assert b.location_of("P1") == "a7"
assert nb.location_of("P1") == "a6"

# rook movements
b = Board()
b = b.move_piece('a2', 'a4')
b = b.move_piece('a1', 'a3')
assert b.location_of("r1") == "a3"
b = b.move_piece('a3', 'f3')
assert b.location_of("r1") == "f3"

# knight movements
b = Board()
b = b.move_piece('b1', 'c3')
assert b.location_of("k1") == "c3"
b = b.move_piece('c3', 'e4')
assert b.location_of("k1") == "e4"

# king movements
b = Board()
b = b.move_piece('e2', 'e4')
b = b.move_piece('e1', 'e2')
assert b.location_of("k") == "e2"
b = b.move_piece('e2', 'f3')
assert b.location_of("k") == "f3"

# queen movements
b = Board()
b = b.move_piece('e2', 'e4')
b = b.move_piece('d1', 'f3')
assert b.location_of("q") == "f3"
# and capture
b = b.move_piece('f3', 'f7')
assert b.location_of("q") == "f7"

# check
b = Board()
b = b.move_piece('e2', 'e4')
b = b.move_piece('d1', 'f3')
b = b.move_piece('f3', 'f7')
assert b.in_check(Board.BLACK) is True
assert b.check_mate(Board.BLACK) is False




print("success!")
