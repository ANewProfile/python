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

# black king safety suffers when there's only white knight
b = Board.custom_board({'k1': 'g2', 'k': 'e1', 'K': 'e6'})
analyzer = DadBoardAnalyzer(b)
assert analyzer.get_king_safety() == 1
b = Board.custom_board({'k1': 'e2', 'k': 'e1', 'K': 'e6'})
analyzer = DadBoardAnalyzer(b)
assert analyzer.get_king_safety() == 2  # control two check positions
b = Board.custom_board({'k1': 'a4', 'k': 'e1', 'K': 'e6'})
analyzer = DadBoardAnalyzer(b)
assert analyzer.get_king_safety() == 1

print("success!")
