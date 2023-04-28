# why it would block a e4->e5 rather than protecting the knight?
#
# based on available pieces, there are threat zones - squares that can cause checks
# those squares have layered importance, based on reachability


from chess import *
board = Board()

class DadBoardAnalyzer(BoardAnalyzer):

    def get_material(self):
        cur_material = 0
        for piece in self.board.pieces():
            if piece_color(piece) == Board.WHITE:
                cur_material += material(piece)
            else:
                cur_material -= material(piece)
        return cur_material

    def get_king_safety(self):
        safety = 0

        white_king_loc = self.board.location_of(get_piece("k", Board.WHITE))
        black_king_loc = self.board.location_of(get_piece("k", Board.BLACK))
        white_king_loc_helper = LocationHelper(white_king_loc)
        black_king_loc_helper = LocationHelper(black_king_loc)

        offsets = (
          (+1, +1),
          (+1, -1),
          (-1, +1),
          (-1, -1),
          (+0, +1),
          (+0, -1),
          (+1, +0),
          (-1, +0),
          (+0, +0)
        )

        king_safety = 0

        for col_offset, row_offset in offsets:
            new_loc, new_loc_piece = white_king_loc_helper.at(col_offset, row_offset, self.board)
            if new_loc:
                if self.board.controlled_by(new_loc, Board.BLACK):
                    king_safety -= 1

            new_loc, new_loc_piece = black_king_loc_helper.at(col_offset, row_offset, self.board)
            if new_loc:
                if self.board.controlled_by(new_loc, Board.WHITE):
                    king_safety += 1

        return king_safety

    def get_piece_risked(self, just_moved_color):
        risked = 0
        for piece, piece_loc in self.board.piece_and_locations():
            if piece_color(piece) == just_moved_color:
                controlling = self.board.controlling_side(piece_loc, just_moved_color)
                if controlling is not None and controlling != just_moved_color:
                    if just_moved_color == Board.WHITE:
                        risked -= (material(piece) if piece not in KINGS else king_material())
                    else:
                        risked += (material(piece) if piece not in KINGS else king_material())
        return risked

    def get_central_controls(self, just_moved_color):
        """
        Returns amount of controlling space, positive favoring white, negative favoring black
        """

        locs = ["d4", "e4", "d5", "e5"]
        space = self.get_controlled_spaces(locs, just_moved_color)*10
        return space

    def get_controlled_spaces(self, locs, just_moved_color):
        """
        Returns amount of controlling space, positive favoring white, negative favoring black
        """

        space = 0
        for square in locs:
            controlling = self.board.controlling_side(square, just_moved_color)
            if controlling == Board.WHITE:
                space += 1
            elif controlling == Board.BLACK:
                space -= 1
        return space

    def compute_score(self, material, risk, king_safety, space):
        """
        Calculates and returns a board evaluation
        """
        score = 0.0
        # material and risk (which is material in immediate danger) are equal weight
        score += material
        score += risk
        score += king_safety
        score += space
        # print(f"m {material} r {risk} k {king_safety} s {space}")

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
            self.get_king_safety(),
            self.get_central_controls(just_moved_color))
