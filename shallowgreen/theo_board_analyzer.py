from chess import *

class TheoBoardAnalyzer(BoardAnalyzer):

    def get_material(self):
        cur_material = 0
        for piece in self.board.pieces():
            if piece_color(piece) == Board.WHITE:
                cur_material += material(piece)
            else:
                cur_material -= material(piece)
        return cur_material

    def get_king_safety(self):

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
            new_loc, _ = white_king_loc_helper.at(
                col_offset, row_offset, self.board)
            if new_loc:
                if self.board.attacked_by(new_loc, Board.BLACK):
                    king_safety -= 1

            new_loc, _ = black_king_loc_helper.at(
                col_offset, row_offset, self.board)
            if new_loc:
                if self.board.attacked_by(new_loc, Board.WHITE):
                    king_safety += 1

        return king_safety

    def get_piece_risked(self, just_moved_color):
        risked = 0
        for piece, piece_loc in self.board.piece_and_locations():
            controlling = self.board.controlling_side(piece_loc, just_moved_color)
            if controlling is not None and controlling != just_moved_color:
                if just_moved_color == Board.WHITE:
                    risked += (material(piece)
                        if piece not in KINGS else king_material())
                else:
                    risked -= (material(piece)
                                if piece not in KINGS else king_material())


        return risked

    def get_central_controls(self, just_moved_color):
        """
        Returns amount of controlling space in center and flank, positive favoring white, negative favoring black
        """

        locs = ["d4", "e4", "d5", "e5", 'c3', 'c4', 'c5', 'c6', 'd3', 'd6', 'e3', 'e6', 'f3', 'f4', 'f5', 'f6']
        space = self.get_controlled_spaces(locs, just_moved_color)*2
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

    def get_space(self, just_moved_color):
        center_and_flank = self.get_central_controls(just_moved_color)
        other_space = self.get_controlled_spaces(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', ' a7', 'a8', 
                                                  'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'
                                                  'c1', 'c2', 'c7', 'c8', 
                                                  'd1', 'd2', 'd7', 'd8',
                                                  'e1', 'e2', 'e7', 'e8',
                                                  'f1', 'f2', 'f7', 'f8',
                                                  'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                                                  'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'], just_moved_color)
        
        return center_and_flank, other_space
    def compute_score(self, material, risk, king_safety, space):
        """
        Calculates and returns a board evaluation
        """
        score = 0.0
        # material and risk (which is material in immediate danger) are equal weight
        score += material
        score += risk
        score += king_safety
        score += space/3
        # print(f"m {material} r {risk} k {king_safety} s {space}")

        # doesn't blunder mate
        for color in (Board.WHITE, Board.BLACK):
            if self.board.check_mate(Board.WHITE):
                score = -1_000_000_000_000_000_000_000_000_000

            if self.board.check_mate(Board.BLACK):
                score = 1_000_000_000_000_000_000_000_000_000

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
        center, other = self.get_space(just_moved_color)
        space = center + other

        return self.compute_score(
            self.get_material(),
            self.get_piece_risked(just_moved_color),
            self.get_king_safety(),
            space)
