from chess import *
from dad_board_analyzer import *
from player import *

player = LookAheadPlayer(DadBoardAnalyzer, depth=2)

board = Board.custom_board({'R1': 'a8', 'K1': 'b8', 'B1': 'c8', 'Q': 'd8', 'K': 'e8', 'B2': 'f8', 'K2': 'g8', 'R2': 'h8', 'P1': 'a7', 'P2': 'b7', 'P3': 'c7', 'P4': 'd7', 'P5': 'e5', 'P6': 'f7', 'P7': 'g7', 'P8': 'h7', 'p5': 'e4', 'p1': 'a2', 'p2': 'b2', 'p3': 'c2', 'p4': 'd2', 'p6': 'f2', 'p7': 'g2', 'p8': 'h2', 'r1': 'a1', 'k1': 'b1', 'b1': 'c1', 'q': 'd1', 'k': 'e1', 'b2': 'f1', 'k2': 'g1', 'r2': 'h1'})
print(board)

# print(player.computer_turn(board, Board.BLACK))

analyzer = DadBoardAnalyzer(board)
print(analyzer.score(Board.BLACK))
