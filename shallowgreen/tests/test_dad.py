from chess import *
from dad_board_analyzer import *
from player import *

# can play
b = Board()
player = LookAheadPlayer(DadBoardAnalyzer)
player.computer_turn(b, Board.WHITE)

# look ahead with depth 2 runs
b = Board()
player = LookAheadPlayer(DadBoardAnalyzer, depth=2)
player.computer_turn(b, Board.WHITE)

print("success!")
