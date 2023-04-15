from chess import *

board = Board()

new_board = board.move_piece("a2", "a3")
assert new_board.piece_at("a2") == None
assert new_board.piece_at("a3") == "p1"

new_board = board.move_piece("e2", "e4")
assert new_board.piece_at("e2") == None
assert new_board.piece_at("e4") == "p5"

new_board = board.move_piece("b1", "c3")
assert new_board.piece_at("b1") == None
assert new_board.piece_at("c3") == "k1"

new_board = board.move_piece("b8", "c6")
assert new_board.piece_at("b8") == None
assert new_board.piece_at("c6") == "K1"

new_board = board.move_piece("e7", "e5")
assert new_board.piece_at("e7") == None
assert new_board.piece_at("e5") == "P5"

board = Board()
print(board)