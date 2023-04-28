from chess import *
from dad_board_analyzer import *
from player import *

player = LookAheadPlayer(DadBoardAnalyzer, depth=2)

board = Board.custom_board(
  {'k': 'e1', 'K': 'e8', 'k1': 'a5', 'Q': 'c6', 'K1': 'c4' }
)
print(board)
analyzer = DadBoardAnalyzer(board)
print("scoring white just moved")
print(analyzer.score(Board.WHITE))
print("scoring black just moved")
print(analyzer.score(Board.BLACK))
