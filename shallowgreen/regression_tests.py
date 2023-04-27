from chess import *
from theo_board_analyzer import *
from look_ahead_player import *

# material
assert material('r1') == 5
assert material('p1') == 1
assert material('b1') == 3
assert material('k1') == 3
assert material('q') == 9

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

# can play
b = Board()
player = LookAheadPlayer(TheoBoardAnalyzer)
player.computer_turn(b, Board.WHITE)

# does not blunder queen
b = Board()
b = b.move_piece('d2', 'd4')
b = b.move_piece('g8', 'f6')
b = b.move_piece('e2', 'e4')
b = b.move_piece('b8', 'c6')
# moving d1h5 would make queen vulnerable to a knight
player = LookAheadPlayer(TheoBoardAnalyzer, depth=1)
move = player.computer_turn(b, Board.WHITE)
assert move[0] != "d1" or move[1] != "h5"

# look ahead with depth 2 runs
b = Board()
player = LookAheadPlayer(TheoBoardAnalyzer, depth=2)
player.computer_turn(b, Board.WHITE)

print("success!")
