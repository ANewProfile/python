# TODO
#
# better safety - safe or not safe from potential threats by specific pieces

from chess import *

class DadBoardAnalyzer(BoardAnalyzer):

    def piece_material(self, piece):
        # a pawn becomes more important as it gets closer to end
        if piece in PAWNS:
            d = rows_to_opp_end(piece, self.board.location_of(piece))
            if d < 2:
                return max(((7-d)*1.0/7)*material("q")/2, material(piece))
        return material(piece) if piece not in KINGS else king_material()

    def get_material(self):
        cur_material = 0
        for piece in self.board.pieces():
            if piece not in KINGS:
                if piece_color(piece) == Board.WHITE:
                    cur_material += self.piece_material(piece)
                else:
                    cur_material -= self.piece_material(piece)
        return cur_material

    def has_pieces(self, color, pieces):
        pieces = list(set([get_piece(p, color) for p in pieces]))
        for p in pieces:
            if self.board.location_of(p) is not None:
                return True
        return False

    def get_piece_risked(self, just_moved_color):
        risked = 0
        next_move_color = Board.WHITE if just_moved_color == Board.BLACK else Board.BLACK

        for piece, piece_loc in self.board.piece_and_locations():
            if piece_color(piece) == just_moved_color:
                piece_control = self.board.controlling_side(piece_loc, just_moved_color)
                if piece_control is not None and piece_control != just_moved_color:
                    # print("%s at %s is vulnerable to %s" % (piece, piece_loc, piece_control))
                    if just_moved_color == Board.WHITE:
                        risked -= self.piece_material(piece)
                    else:
                        risked += self.piece_material(piece)
        return risked

    def get_central_controls(self, just_moved_color):
        """
        Returns amount of controlling space, positive favoring white, negative favoring black
        """

        spaces = 0

        locs = ["c5", "d5", "e5", "f5"]
        spaces += self.get_controlled_spaces(locs, Board.WHITE, just_moved_color)
        locs = ["c4", "d4", "e4", "f4"]
        spaces -= self.get_controlled_spaces(locs, Board.BLACK, just_moved_color)
        return spaces

    def get_controlled_spaces(self, locs, color, just_moved_color):
        """
        Returns number of spaces controlled by the specified color
        """

        spaces = 0
        for square in locs:
            if self.board.controlling_side(square, just_moved_color) == color:
                spaces += 1
        return spaces

    def compute_score(self, material, risk, safety, center_controls):
        """
        Calculates and returns a board evaluation
        """
        score = 0.0
        # material and risk (which is material in immediate danger) are equal weight
        score += material
        score += risk
        score += safety
        score += center_controls/2
        if DEBUG_MOVE:
           print(f"m {material} r {risk} s {safety} c {center_controls}")

        # doesn't blunder mate
        for color in (Board.WHITE, Board.BLACK):
            if self.board.check_mate(Board.WHITE):
                score = -1_000_000_000_000_000

            if self.board.check_mate(Board.BLACK):
                score = 1_000_000_000_000_000

        return score

    @staticmethod
    def better_score(color, a, b):
        """
        Returns better value of a or b, depends on the specified color
        """

        return max(a, b) if color == Board.WHITE else min(a, b)

    @staticmethod
    def worse_score(color, a, b):
        """
        Returns worse value of a or b, depends on the specified color
        """

        return min(a, b) if color == Board.WHITE else max(a, b)

    def score(self, just_moved_color):
        """
        Returns a numeric score bassed off of the compute_score() func
        """

        return self.compute_score(
            self.get_material(),
            self.get_piece_risked(just_moved_color),
            0,
            self.get_central_controls(just_moved_color))
