from chess import *

class DadBoardAnalyzer(BoardAnalyzer):

    def piece_material(self, piece):
        # a pawn becomes more important as it gets closer to end
        if piece in PAWNS:
            d = rows_to_opp_end(piece, self.board.location_of(piece))
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

    def get_safety_with_offsets(self, start_loc, offsets, color):
        """
	Returns safety for a set of locations, positive favoring white,
	negative favoring black. The absoluate safety value is a float between
        0 and 1 representing fraction of the locations that are safe.
        """

        safe_locations = 0
        checked_locations = 0
        loc_helper = LocationHelper(start_loc)
        opp_color = Board.WHITE if color == Board.BLACK else Board.BLACK

        for col_offset, row_offset in offsets:
            new_loc, new_loc_piece = loc_helper.at(col_offset, row_offset, self.board)
            if new_loc:
                checked_locations += 1
                if not self.board.attacked_by(new_loc, opp_color):
                    safe_locations += 1

        safety = safe_locations*1.0/checked_locations
        if color == Board.WHITE:
            return safety
        else:
            return -1*safety
        return safety

    def has_pieces(self, color, pieces):
        pieces = list(set([get_piece(p, color) for p in pieces]))
        for p in pieces:
            if self.board.location_of(p) is not None:
                return True
        return False

    def get_safety(self, piece_name):
        """
	Returns relative, combined safety for both side for the piece, positive
	favoring white, negative favoring black. The absoluate safety value is
        a float between 0 and 1.
        """

        safety = 0

        white_loc = self.board.location_of(get_piece(piece_name, Board.WHITE))
        black_loc = self.board.location_of(get_piece(piece_name, Board.BLACK))

        white_offsets = [ (+0, +0) ]
        black_offsets = [ (+0, +0) ]

        if self.has_pieces(Board.BLACK, KNIGHTS):
            white_offsets.extend([ (-2, -1), (-2, +1), (-1, -2), (-1, +2),
                                   (+2, -1), (+2, +1), (+1, -2), (+1, +2) ])
        if self.has_pieces(Board.WHITE, KNIGHTS):
            black_offsets.extend([ (-2, -1), (-2, +1), (-1, -2), (-1, +2),
                                   (+2, -1), (+2, +1), (+1, -2), (+1, +2) ])

        if self.has_pieces(Board.BLACK, ["B1"]) and white_loc and loc_is_white(white_loc):
            white_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
        if self.has_pieces(Board.BLACK, ["B2"]) and white_loc and loc_is_black(white_loc):
            white_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
        if self.has_pieces(Board.WHITE, ["b1"]) and black_loc and loc_is_black(black_loc):
            black_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
        if self.has_pieces(Board.WHITE, ["b2"]) and black_loc and loc_is_white(black_loc):
            black_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])

        if self.has_pieces(Board.BLACK, ROOKS):
            white_offsets.extend([ (-2, 0), (+2, 0), (-1, 0), (+1, 0),
                                   (0, -2), (0, +2), (0, -1), (0, +1) ])
        if self.has_pieces(Board.WHITE, ROOKS):
            black_offsets.extend([ (-2, 0), (+2, 0), (-1, 0), (+1, 0),
                                   (0, -2), (0, +2), (0, -1), (0, +1) ])

        if self.has_pieces(Board.BLACK, QUEENS):
            white_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
            white_offsets.extend([ (-2, 0), (+2, 0), (-1, 0), (+1, 0),
                                   (0, -2), (0, +2), (0, -1), (0, +1) ])
        if self.has_pieces(Board.WHITE, QUEENS):
            black_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
            black_offsets.extend([ (-2, 0), (+2, 0), (-1, 0), (+1, 0),
                                   (0, -2), (0, +2), (0, -1), (0, +1) ])

        if self.has_pieces(Board.BLACK, PAWNS):
            white_offsets.extend([ (-1, -1), (-1, +1), (+1, -1), (+1, +1)])
        if self.has_pieces(Board.WHITE, PAWNS):
            black_offsets.extend([ (-1, -1), (-1, +1), (+1, -1), (+1, +1)])

        if self.has_pieces(Board.BLACK, KINGS):
            white_offsets.extend([ (-1, -1), (-1, +1), (+1, -1), (+1, +1)])
            white_offsets.extend([ (-1, 0), (+1, 0), (0, -1), (0, +1) ])
        if self.has_pieces(Board.WHITE, KINGS):
            black_offsets.extend([ (-1, -1), (-1, +1), (+1, -1), (+1, +1)])
            black_offsets.extend([ (-1, 0), (+1, 0), (0, -1), (0, +1) ])

        white_offsets = list(set(white_offsets))
        black_offsets = list(set(black_offsets))

        safety = 0
        if white_loc:
            safety += self.get_safety_with_offsets(white_loc, white_offsets, Board.WHITE)
        if black_loc:
            safety += self.get_safety_with_offsets(black_loc, black_offsets, Board.BLACK)

        return safety

    def get_piece_risked(self, just_moved_color):
        risked = 0
        next_move_color = Board.WHITE if just_moved_color == Board.BLACK else Board.BLACK

        for piece, piece_loc in self.board.piece_and_locations():
            if piece_color(piece) == just_moved_color:
                if self.board.attacked_by(piece_loc, next_move_color):
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
            if self.board.attacked_by(square, color):
                spaces += 1
        # print("%s controls %s? %s" % (color, locs, spaces))
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
        # print(f"m {material} r {risk} s {safety} c {center_controls}")

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
            self.get_safety("k")*5 + self.get_safety("q")*5 + self.get_safety("r")*3,
            self.get_central_controls(just_moved_color))
