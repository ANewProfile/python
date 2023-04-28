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
                if self.board.controlled_by(new_loc, Board.BLACK):
                    king_safety -= 1

            new_loc, _ = black_king_loc_helper.at(
                col_offset, row_offset, self.board)
            if new_loc:
                if self.board.controlled_by(new_loc, Board.WHITE):
                    king_safety += 1

        return king_safety

    def get_piece_risked(self, just_moved_color):
        risked = 0
        for piece, piece_loc in self.board.piece_and_locations():
            controlling = self.board.controlling_side(piece_loc)
            if controlling is not None and controlling != just_moved_color:
                if just_moved_color == Board.WHITE:
                    for move in self.board.possible_moves(piece_loc):
                        print(piece_loc, move)
                        try:
                            new_board = self.board.move_piece(piece_loc, move)
                        except InvalidMoveException:
                            continue
                        if new_board.controlling_side(move) == Board.BLACK:
                            risked += (material(piece)
                                if piece not in KINGS else king_material())
                else:
                    for move in self.board.possible_moves(piece_loc):
                        print(piece_loc, move)
                        print("on")
                        print(self.board)
                        try:
                            new_board = self.board.move_piece(piece_loc, move)
                        except InvalidMoveException:
                            continue
                        print("results in")
                        print(new_board)
                        if new_board.controlling_side(move) == Board.WHITE:
                            risked -= (material(piece)
                                       if piece not in KINGS else king_material())


            elif controlling is not None and controlling == just_moved_color:
                if just_moved_color == Board.WHITE:
                    for move in self.board.possible_moves(piece_loc):
                        try:
                            new_board = self.board.move_piece(piece_loc, move)
                        except InvalidMoveException:
                            continue
                        if new_board.controlling_side(move) == Board.BLACK:
                            risked -= (material(piece)
                                       if piece not in KINGS else king_material())*0.25
                else:
                    for move in self.board.possible_moves(piece_loc):
                        try:
                            new_board = self.board.move_piece(piece_loc, move)
                        except InvalidMoveException:
                            continue
                        if new_board.controlling_side(move) == Board.WHITE:
                            risked += (material(piece)
                                       if piece not in KINGS else king_material())*0.25

        return risked

    def get_central_controls(self):
        """
        Returns amount of controlling space, positive favoring white, negative favoring black
        """

        locs = ["d4", "e4", "d5", "e5"]
        space = self.get_controlled_spaces(locs)*2
        return space

    def get_controlled_spaces(self, locs):
        """
        Returns amount of controlling space, positive favoring white, negative favoring black
        """

        space = 0
        for square in locs:
            controlling = self.board.controlling_side(square)
            if controlling == Board.WHITE:
                space += 1
            elif controlling == Board.BLACK:
                space -= 1
        return space

    def compute_score(self, material, risk, king_safety, space, board):
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
            if board.check_mate(Board.WHITE):
                score = -1_000_000_000_000_000_000_000_000_000

            if board.check_mate(Board.BLACK):
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

    def score(self, just_moved_color, board):
        """
        Returns a numeric score bassed off of the compute_score() func
        """

        return self.compute_score(
            self.get_material(),
            self.get_piece_risked(just_moved_color),
            self.get_king_safety(),
            self.get_central_controls(),
            board)
