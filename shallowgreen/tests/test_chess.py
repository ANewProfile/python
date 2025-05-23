from chess import *

# material
assert material('r1') == 5
assert material('p1') == 1
assert material('b1') == 3
assert material('k1') == 3
assert material('q') == 9

# color of location
assert loc_is_white('a1') is False
assert loc_is_white('a2') is True
assert loc_is_black('a1') is True
assert loc_is_black('a2') is False
assert loc_is_white('b1') is True
assert loc_is_white('b2') is False
assert loc_is_black('b1') is False
assert loc_is_black('b2') is True

# pawn movements
b = Board()
nb = b.move_piece('e2', 'e4')
assert b.location_of("p5") == "e2"
assert nb.location_of("p5") == "e4"
nb = b.move_piece('a7', 'a6')
assert b.location_of("P1") == "a7"
assert nb.location_of("P1") == "a6"

# pawn cannot move two spaces over something
b = Board()
b = b.move_piece('b1', 'c3')
try:
  b = b.move_piece('c2', 'c4')
except InvalidMoveException:
  pass
else:
  assert False 

# pawn can take left and right
b = Board.custom_board({'p1': 'e2', 'R1': 'd3', 'R2': 'f3', 'B1': 'e3', 'k': 'a1', 'K': 'h8'})
assert b.location_of("R1") is not None
b = b.move_piece("e2", "d3")
assert b.location_of("p1") == "d3"
assert b.location_of("R1") is None
b = Board.custom_board({'p1': 'e2', 'R1': 'd3', 'R2': 'f3', 'B1': 'e3', 'k': 'a1', 'K': 'h8'})
assert b.location_of("R2") is not None
b = b.move_piece("e2", "f3")
assert b.location_of("p1") == "f3"
assert b.location_of("R2") is None

# pawn cannot take its own piece
b = Board.custom_board({'p1': 'e2', 'R1': 'd3', 'r2': 'f3', 'B1': 'e3', 'k': 'a1', 'K': 'h8'})
try:
  b = b.move_piece("e2", "f3")
except InvalidMoveException:
  pass
else:
  assert False 

# pawn cannot take straight ahead
b = Board.custom_board({'p1': 'e2', 'R1': 'd3', 'R2': 'f3', 'B1': 'e3', 'k': 'a1', 'K': 'h8'})
try:
  b = b.move_piece('e2', 'e3')
except InvalidMoveException:
  pass
else:
  assert False 

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

# does not move into check
b = Board()
b = b.move_piece('e2', 'e4')
b = b.move_piece('d1', 'f3')
b = b.move_piece('f3', 'h5')
try:
    b = b.move_piece('f7', 'f6')  # moves K into checked position
except InvalidMoveException:
    pass
else:
    assert False

# promotion on pawn moving up
b = Board.custom_board({'p1': 'e7', 'k': 'e1', 'K': 'a8'})
b = b.move_piece("e7", "e8", promotion='q')
assert b.location_of("q") == "e8"
assert len(b.pieces()) == 3
assert "q" in b.pieces()
assert "k" in b.pieces()
assert "K" in b.pieces()

# promotion on pawn take
b = Board.custom_board({'p1': 'e7', 'R1': 'd8', 'k': 'e1', 'K': 'a8'})
b = b.move_piece("e7", "d8", promotion='q')
assert b.location_of("q") == "d8"
assert len(b.pieces()) == 3
assert "q" in b.pieces()
assert "k" in b.pieces()
assert "K" in b.pieces()

# a piece can be protected by its own bishop even when the piece is "blocking"
# the bishop
b = Board()
b = b.move_piece("e2", "e4")
b = b.move_piece("f1", "b5")
assert b.attacked_by("d7", Board.WHITE) is True

# protected by its own bishop even when the piece is "blocking" the bishop
b = Board()
b = Board.custom_board({'b1': 'b5', 'P1': 'd7', 'B1': 'c8', 'k': 'e1', 'K': 'e8'})
assert b.attacked_by("d7", Board.WHITE) is True
assert b.controlling_side("d7", Board.WHITE) is Board.BLACK

# no control if both sides have same number of pieces attacking the location
b = Board()
b = Board.custom_board({'b1': 'b5', 'P1': 'd7', 'B1': 'c8', 'k': 'f1', 'K': 'f8'})
assert b.attacked_by("d7", Board.WHITE) is True
assert b.controlling_side("d7", Board.WHITE) is None

print("success!")
