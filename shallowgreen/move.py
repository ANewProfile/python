from chess import *

class Move(object):
    """
    Represents a move, which is an actual move (old_location, new_location)
    tuple, a resulting board, and the side that moved.
    """

    def __init__(self, move, new_board, just_moved_color):
        self.move = move
        self.new_board = new_board
        self.just_moved_color = just_moved_color

    @property
    def next_move_color(self):
        return Board.WHITE if self.just_moved_color == Board.BLACK else Board.BLACK