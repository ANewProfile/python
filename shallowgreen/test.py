from chess import *
from theo_board_analyzer import *
from player import *

player = LookAheadPlayer(TheoBoardAnalyzer, depth=2)

board = Board.custom_board({'R1': 'a8', 'K1': 'b8', 'B1': 'c8', 'K': 'e8', 'K2': 'g8', 'R2': 'h8', 'P1': 'a7', 'P2': 'b7', 'P3': 'c7', 'P4': 'd7', 'P6': 'f7', 'P7': 'g7', 'P8': 'h7', 'P5': 'e6', 'Q': 'g5', 'B2': 'b4', 'p4': 'd4', 'q': 'd3', 'p1': 'a2', 'p2': 'b2', 'p3': 'c2', 'p5': 'e2', 'p6': 'f2', 'p7': 'g2', 'p8': 'h2', 'r1': 'a1', 'k1': 'b1', 'k': 'e1', 'b2': 'f1', 'k2': 'g1', 'r2': 'h1'})
print(board)
move = player.computer_turn(board, Board.WHITE)
print(move)
