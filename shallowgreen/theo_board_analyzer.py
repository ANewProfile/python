from chess import *
board = Board()

class TheoBoardAnalyzer(BoardAnalyzer):

    def get_material(self):
        cur_material = 0
        for piece in self.board.pieces():
            if piece_color(piece) == Board.WHITE:
                cur_material += material(piece)
            else:
                cur_material -= material(piece)
        return cur_material

    def get_safety(self):
        safety = 0

        white_king_loc = self.board.location_of('k')
        black_king_loc = self.board.location_of('K')
        white_king_pos = loc_to_col_row(white_king_loc)
        black_king_pos = loc_to_col_row(black_king_loc)

        around_king_white = [
          [white_king_pos[0]+1, white_king_pos[1]+1],
          [white_king_pos[0]+1, white_king_pos[1]-1],
          [white_king_pos[0]-1, white_king_pos[1]+1],
          [white_king_pos[0]-1, white_king_pos[1]-1],
          [white_king_pos[0]+1, white_king_pos[1]],
          [white_king_pos[0], white_king_pos[1]+1],
          [white_king_pos[0]-1, white_king_pos[1]],
          [white_king_pos[0], white_king_pos[1]-1]
        ]

        around_king_black = [
          [black_king_pos[0]+1, black_king_pos[1]+1],
          [black_king_pos[0]+1, black_king_pos[1]-1],
          [black_king_pos[0]-1, black_king_pos[1]+1],
          [black_king_pos[0]-1, black_king_pos[1]-1],
          [black_king_pos[0]+1, black_king_pos[1]],
          [black_king_pos[0], black_king_pos[1]+1],
          [black_king_pos[0]-1, black_king_pos[1]],
          [black_king_pos[0], black_king_pos[1]-1]
        ]

        locs_around_king_white = [col_row_to_loc(col_row) for col_row in around_king_white
                                  if col_row[0] < 8 and col_row[0] > -1 and col_row[1] < 8 and col_row[1] >= 0]

        locs_around_king_black = [col_row_to_loc(col_row) for col_row in around_king_black
                                  if col_row[0] < 8 and col_row[0] >= 0 and col_row[1] < 8 and col_row[1] >= 0]

        space_white = self.specific_space(locs_around_king_white)
        space_black = self.specific_space(locs_around_king_black)

        if space_white < 0:
            safety -= space_white
        if space_black > 0:
            safety += space_black

        return safety

    def get_piece_risked(self, just_moved_color):
        risked = 0
        for piece in self.board.pieces():
            if piece_color(piece) == just_moved_color:
                controlling = self.board.controlling_side(
                    self.board.location_of(piece))
                if controlling is not None and controlling != just_moved_color:
                    if just_moved_color == Board.WHITE:
                        risked -= material(piece)
                    else:
                        risked += material(piece)
        return risked

    def get_space(self):
        """
        Returns amount of controlling space, positive favoring white, negative favoring black
        """

        all_spaces = [col_row_to_loc([c, r])
                      for c in range(8) for r in range(8)]

        return self.specific_space(all_spaces)

    def specific_space(self, locs):
        """
        Returns amount of controlling space, positive favoring white, negative favoring black
        """

        space = 0
        for square in locs:
            controlling = self.board.controlling_side(square)
            if controlling == Board.WHITE:
                if square[0] in ('d', 'e'):
                    space += 3
                elif square[0] in ('c', 'f'):
                    space += 2
                else:
                    space += 1
            elif controlling == Board.BLACK:
                if square[0] in ('d', 'e'):
                    space -= 3
                elif square[0] in ('c', 'f'):
                    space -= 2
                else:
                    space -= 1
        return space

    def compute_score(self, material, safety, space, risk, board):
        """
        Calculates and returns a board evaluation"""
        score = 0.0
        # material and risk (which is material in immediate danger) are equal weight
        score += material
        score += risk
        score += safety
        # space is less
        score += space/3

        # doesn't blunder mate
        for color in (Board.WHITE, Board.BLACK):
            if board.check_mate(Board.WHITE):
                score = -1_000_000_000_000_000

            if board.check_mate(Board.BLACK):
                score = 1_000_000_000_000_000

        return score

    @staticmethod
    def better_score(self, color, a, b):
        """
        Returns better value of a or b, depends on the specified color
        """

        return max(a, b) if color == Board.WHITE else min(a, b)

    @staticmethod
    def worse_score(self, color, a, b):
        """
        Returns worse value of a or b, depends on the specified color
        """

        return min(a, b) if color == Board.WHITE else max(a, b)

    def score(self, just_moved_color, board):
        """
        Returns a numeric score bassed off of the compute_score() func
        """
        space = self.get_space()
        risked = self.get_piece_risked(just_moved_color)
        # print("material", self.get_material(), "safety", self.get_safety(), "sp", space, "risked", risked)
        return self.compute_score(
            self.get_material(),
            self.get_safety(),
            space, risked, board)
