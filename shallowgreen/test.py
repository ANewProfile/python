from chess import *

board = Board()

new_board = board.move_piece("a2", "a3")
assert new_board.piece_at("a2") == None
assert new_board.piece_at("a3").piece == "p1"

new_board = board.move_piece("e2", "e4")
assert new_board.piece_at("e2") == None
assert new_board.piece_at("e4").piece == "p5"

new_board = board.move_piece("b1", "c3")
assert new_board.piece_at("b1") == None
assert new_board.piece_at("c3").piece == "k1"

new_board = board.move_piece("b8", "c6")
assert new_board.piece_at("b8") == None
assert new_board.piece_at("c6").piece == "K1"

new_board = board.move_piece("e7", "e5")
assert new_board.piece_at("e7") == None
assert new_board.piece_at("e5").piece == "P5"

board = Board()
board = board.move_piece("d2", "d4")
board = board.move_piece("d7", "d5")
board = board.move_piece("c2", "c4")
board = board.move_piece("d5", "c4")
board = board.move_piece("e2", "e4")
board = board.move_piece("d8", "d4")
print(board)
