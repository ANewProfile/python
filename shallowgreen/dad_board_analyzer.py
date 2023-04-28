# TODO
#
# why it would block a e4->e5 rather than protecting the knight?
#
# based on available pieces, there are threat zones - squares that can cause checks
# those squares have layered importance, based on reachability

from chess import *

class DadBoardAnalyzer(BoardAnalyzer):

    def get_material(self):
        cur_material = 0
        for piece in self.board.pieces():
            if piece_color(piece) == Board.WHITE:
                cur_material += material(piece)
            else:
                cur_material -= material(piece)
        return cur_material

    def get_safety(self, start_loc, offsets, color):
        safety = 0
        loc_helper = LocationHelper(start_loc)
        opp_color = Board.WHITE if color == Board.BLACK else Board.BLACK

        for col_offset, row_offset in offsets:
            new_loc, new_loc_piece = loc_helper.at(col_offset, row_offset, self.board)
            if new_loc:
                if self.board.controlled_by(new_loc, opp_color):
                    if color == Board.WHITE:
                        safety -= 1
                    else:
                        safety += 1

        # print("safety of %s for %s: %s" % (start_loc, color, safety))
        return safety

    def has_pieces(self, color, pieces):
        pieces = list(set([get_piece(p, color) for p in pieces]))
        for p in pieces:
            if self.board.location_of(p) is not None:
                return True
        return False

    def get_king_safety(self):
        safety = 0

        white_king_loc = self.board.location_of(get_piece("k", Board.WHITE))
        black_king_loc = self.board.location_of(get_piece("k", Board.BLACK))

        white_offsets = [ (+0, +0) ]
        black_offsets = [ (+0, +0) ]

        if self.has_pieces(Board.BLACK, KNIGHTS):
            white_offsets.extend([ (-2, -1), (-2, +1), (-1, -2), (-1, +2),
                                   (+2, -1), (+2, +1), (+1, -2), (+1, +2) ])
        if self.has_pieces(Board.WHITE, KNIGHTS):
            black_offsets.extend([ (-2, -1), (-2, +1), (-1, -2), (-1, +2),
                                   (+2, -1), (+2, +1), (+1, -2), (+1, +2) ])

        if self.has_pieces(Board.BLACK, ["B1"]) and loc_is_white(white_king_loc):
            white_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
        if self.has_pieces(Board.BLACK, ["B2"]) and loc_is_black(white_king_loc):
            white_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
        if self.has_pieces(Board.WHITE, ["b1"]) and loc_is_black(black_king_loc):
            black_offsets.extend([ (-1, -1), (-1, +1), (-2, -2), (-2, +2),
                                   (+1, -1), (+1, +1), (+2, -2), (+2, +2) ])
        if self.has_pieces(Board.WHITE, ["b2"]) and loc_is_white(black_king_loc):
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

        king_safety = self.get_safety(white_king_loc, white_offsets, Board.WHITE) + \
                      self.get_safety(black_king_loc, black_offsets, Board.BLACK)
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
        space = self.get_controlled_spaces(locs, just_moved_color)
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

    def compute_score(self, material, risk, king_safety, center_controls):
        """
        Calculates and returns a board evaluation
        """
        score = 0.0
        # material and risk (which is material in immediate danger) are equal weight
        score += material
        score += risk
        score += king_safety/10
        score += center_controls/2
        # print(f"m {material} r {risk} k {king_safety} s {center_controls}")

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
