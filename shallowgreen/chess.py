def loc_to_col_row(loc):
    return ord(loc[0])-ord('a'), int(loc[1])-1


def col_row_to_loc(pos):
    return "".join([chr(ord('a') + pos[0]), str(pos[1]+1)])


pawns = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
         'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8')
rooks = ('r1', 'r2', 'R1', 'R2')
bishops = ('b1', 'b2', 'B1', 'B2')
knights = ('k1', 'k2', 'K1', 'K2')
queens = ('q', 'Q')
kings = ('k', 'K')


def material(piece):
    if piece in pawns:
        return 1
    elif piece in rooks:
        return 5
    elif piece in bishops or piece in knights:
        return 3
    elif piece in queens:
        return 9
    else:
        return 0


class LocationHelper(object):

    def __init__(self, loc):
        self.loc = loc
        self.col_row = loc_to_col_row(loc)

    def at(self, col_offset, row_offset, board):
        # returns (loc, piece) tuple
        # if offset moves position off the board, returns (None, None)

        new_col = self.col_row[0] + col_offset
        new_row = self.col_row[1] + row_offset
        if new_col >= 0 and new_col < 8 and new_row >= 0 and new_row < 8:
            new_loc = col_row_to_loc([new_col, new_row])
            return [new_loc, board.piece_at(new_loc)]
        else:
            return [None, None]


def piece_color(piece):
    if piece == "" or piece is None:
        return None
    return Board.WHITE if piece.islower() else Board.BLACK


def white_color_of(piece):
    return piece.lower()


def black_color_of(piece):
    return piece.upper()


class Board(object):
    WHITE = "white"
    BLACK = "black"

    def find_locations(self):
        self.piece_locations = {}
        for i, array in enumerate(self.positions):
            for j, piece in enumerate(array):
                if piece is not None:
                    row = 7 - i
                    col = j
                    loc = col_row_to_loc([col, row])
                    self.piece_locations[piece] = loc

    def location_of(self, piece):
        if self.piece_locations is None:
            self.find_locations()
        return self.piece_locations[piece]

    def pieces(self):
        if self.piece_locations is None:
            self.find_locations()
        return self.piece_locations.keys()

    def piece_at(self, loc):
        pos = loc_to_col_row(loc)
        return self.positions[7-pos[1]][pos[0]]

    def set_piece_at(self, piece, loc):
        pos = loc_to_col_row(loc)
        self.positions[7-pos[1]][pos[0]] = piece
        self.piece_locations = None

    def controlling_side(self, loc):
        pieces_guarding = 0
        for piece in self.pieces():
            if loc in self.possible_moves(self.location_of(piece)):
                if piece_color(piece) == Board.BLACK:
                    pieces_guarding -= 1
                else:
                    pieces_guarding += 1
        if pieces_guarding > 0:
            return Board.WHITE
        elif pieces_guarding < 0:
            return Board.BLACK
        else:
            return None

    def __str__(self):
        return "\n".join(
            [" | ".join(["  " if piece is None else "%2s" % (piece)
                        for piece in sub_array]) for sub_array in self.positions]
        )

    def __init__(self):
        self.positions = [[None for i in range(8)] for j in range(8)]
        self.piece_locations = None
        self.white_can_castle_right = True
        self.black_can_castle_right = True
        self.white_can_castle_left = True
        self.black_can_castle_left = True

        # set board, initial position for white pieces
        self.set_piece_at("r1", "a1")
        self.set_piece_at("k1", "b1")
        self.set_piece_at("b1", "c1")
        self.set_piece_at("q",  "d1")
        self.set_piece_at("k",  "e1")
        self.set_piece_at("b2", "f1")
        self.set_piece_at("k2", "g1")
        self.set_piece_at("r2", "h1")
        self.set_piece_at("p1", "a2")
        self.set_piece_at("p2", "b2")
        self.set_piece_at("p3", "c2")
        self.set_piece_at("p4", "d2")
        self.set_piece_at("p5", "e2")
        self.set_piece_at("p6", "f2")
        self.set_piece_at("p7", "g2")
        self.set_piece_at("p8", "h2")

        # set board, initial position for black pieces
        self.set_piece_at("R1", "a8")
        self.set_piece_at("K1", "b8")
        self.set_piece_at("B1", "c8")
        self.set_piece_at("Q",  "d8")
        self.set_piece_at("K",  "e8")
        self.set_piece_at("B2", "f8")
        self.set_piece_at("K2", "g8")
        self.set_piece_at("R2", "h8")
        self.set_piece_at("P1", "a7")
        self.set_piece_at("P2", "b7")
        self.set_piece_at("P3", "c7")
        self.set_piece_at("P4", "d7")
        self.set_piece_at("P5", "e7")
        self.set_piece_at("P6", "f7")
        self.set_piece_at("P7", "g7")
        self.set_piece_at("P8", "h7")

    def loc_piece_color(self, loc):
        piece = self.piece_at(loc)
        return piece_color(piece)

    def get_material(self):
        cur_material = 0
        for piece in self.pieces():
            if piece_color(piece) == Board.WHITE:
                cur_material += material(piece)
            else:
                cur_material -= material(piece)
        return cur_material

    def get_safety(self):
        safety = 0

        white_king_loc = self.location_of('k')
        black_king_loc = self.location_of('K')
        white_king_pos = loc_to_col_row(white_king_loc)
        black_king_pos = loc_to_col_row(black_king_loc)

        around_king_white = [[white_king_pos[0]+1, white_king_pos[1]+1], [white_king_pos[0]+1, white_king_pos[1]-1], [white_king_pos[0]-1, white_king_pos[1]+1],
                             [white_king_pos[0]-1, white_king_pos[1]-1], [white_king_pos[0]+1,
                                                                          white_king_pos[1]], [white_king_pos[0], white_king_pos[1]+1],
                             [white_king_pos[0]-1, white_king_pos[1]], [white_king_pos[0], white_king_pos[1]-1]]

        around_king_black = [[black_king_pos[0]+1, black_king_pos[1]+1], [black_king_pos[0]+1, black_king_pos[1]-1], [black_king_pos[0]-1, black_king_pos[1]+1],
                             [black_king_pos[0]-1, black_king_pos[1]-1], [black_king_pos[0]+1,
                                                                          black_king_pos[1]], [black_king_pos[0], black_king_pos[1]+1],
                             [black_king_pos[0]-1, black_king_pos[1]], [black_king_pos[0], black_king_pos[1]-1]]

        locs_around_king_white = [col_row_to_loc(col_row) for col_row in around_king_white
                                  if col_row[0] < 8 and col_row[0] > -1 and col_row[1] < 8 and col_row[1] >= 0]

        locs_around_king_black = [col_row_to_loc(col_row) for col_row in around_king_black
                                  if col_row[0] < 8 and col_row[0] >= 0 and col_row[1] < 8 and col_row[1] >= 0]

        space_white = self.specific_space(locs_around_king_white)
        space_black = self.specific_space(locs_around_king_black)

        if space_white[0] < 0:
            safety += space_white[0] * 0.95
            safety += space_white[1] * 0.5

        if space_black[0] < 0:
            safety -= space_black[0] * 0.95
            safety -= space_black[1] * 0.5

        return safety

    def get_space(self):
        """
        Returns amount of controlling space and risk for each color, positive for white, negative for black
        """

        all_spaces = [col_row_to_loc([c, r])
                      for c in range(8) for r in range(8)]

        return self.specific_space(all_spaces)

    def get_piece_risked(self, just_moved_color):
        risked = 0
        for piece in self.pieces():
            if piece_color(piece) == just_moved_color:
                controlling = self.controlling_side(self.location_of(piece))
                if controlling is not None and controlling != just_moved_color:
                    if just_moved_color == Board.WHITE:
                        risked -= material(piece)
                    else:
                        risked += material(piece)
        return risked

    def specific_space(self, locs):
        """
        Returns amount of controlling space and risk for each color, positive for white, negative for black
        """

        space = 0
        risked = 0
        for square in locs:
            square_col_row = loc_to_col_row(square)
            piece = self.piece_at(square)
            piece_clr = piece_color(piece)
            controlling = self.controlling_side(square)
            if piece is not None:
                if controlling == Board.WHITE and piece_clr == Board.BLACK:
                    risked += material(piece)  # black piece controlled by white, good for white
                elif controlling == Board.BLACK and piece_clr == Board.WHITE:
                    risked -= material(piece)  # white piece controlled by black, good for black
            else:
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
        return space, risked

    def compute_score(self, material, safety, space, risk):
        score = 0.0
        # material and risk (which is material in immediate danger) are equal weight
        score += material
        score += risk
        score += safety
        # space is less
        score += space/2
        return score

    def score(self, just_moved_color):
        space, captures = self.get_space()
        risk = self.get_piece_risked(just_moved_color)
        # print("material", self.get_material(), "safety", self.get_safety(), "sp", space, "cap", captures, "risk", risk)
        return self.compute_score(
            self.get_material(),
            self.get_safety(),
            space+captures, risk)

    def computer_turn(self, color):
        best_score = None
        best_move = None
        best_old_loc = None
        cur_score = 0
        pieces = self.pieces()

        for piece in pieces:
            piece_clr = piece_color(piece)
            old_location = self.location_of(piece)
            if piece_clr == color:
                for move in self.possible_moves(old_location):
                    # print("computer wants to move", (old_location, move))
                    try:
                        new_board = self.move_piece(old_location, move)
                    except Exception as e:
                        # print("  disallowed (%s)" % str(e))
                        continue
                    cur_score = new_board.score(color)
                    # print("scoring", old_location, "to", move, "score is", cur_score)
                    if (color == Board.WHITE and (best_score is None or cur_score > best_score)) or \
                            (color == Board.BLACK and (best_score is None or cur_score < best_score)):
                        best_score = cur_score
                        best_old_loc = old_location
                        best_move = move

        if best_move is None:  # cannot make a move
            if self.check_mate(color):
                raise Exception("Checkmate, %s lost" % color)
            else:
                raise Exception("Draw")
        return best_old_loc, best_move

    def diagonal_moves(self, piece, loc, total_range):

        loc_helper = LocationHelper(loc)
        cont = [True, True, True, True]
        new_locations = []

        for i in range(1, total_range):
            if cont[0] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, -i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[0] = False

            if cont[1] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, +i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[1] = False

            if cont[2] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, -i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[2] = False

            if cont[3] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, +i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[3] = False

        return new_locations

    def cross_moves(self, piece, loc, total_range):

        loc_helper = LocationHelper(loc)
        cont = [True, True, True, True]
        new_locations = []

        for i in range(1, total_range):
            if cont[0] is True:
                new_loc, new_loc_piece = loc_helper.at(0, -i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[0] = False

            if cont[1] is True:
                new_loc, new_loc_piece = loc_helper.at(0, +i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[1] = False

            if cont[2] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, 0, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[2] = False

            if cont[3] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, 0, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[3] = False

        return new_locations

    def pawn_moves(self, piece, loc):
        loc_helper = LocationHelper(loc)
        cur_col, cur_row = loc_to_col_row(loc)
        new_locations = []
        piece_clr = self.loc_piece_color(loc)

        if piece_clr == Board.WHITE:  # white moves
            new_loc, new_loc_piece = loc_helper.at(0, 1, self)
            if new_loc is not None and new_loc_piece is None:
                new_locations.append(new_loc)
            if cur_row == 1:
                new_loc, new_loc_piece = loc_helper.at(0, 2, self)
                if new_loc is not None and new_loc_piece is None:
                    new_locations.append(new_loc)
            # take right!
            new_loc, new_loc_piece = loc_helper.at(+1, +1, self)
            if new_loc is not None and new_loc_piece is not None and piece_color(new_loc_piece) == Board.BLACK:
                new_locations.append(new_loc)
            # take left!
            new_loc, new_loc_piece = loc_helper.at(-1, +1, self)
            if new_loc is not None and new_loc_piece is not None and piece_color(new_loc_piece) == Board.BLACK:
                new_locations.append(new_loc)

        else:  # black moves
            new_loc, new_loc_piece = loc_helper.at(0, -1, self)
            if new_loc is not None and new_loc_piece is None:
                new_locations.append(new_loc)
            elif cur_row == 6:
                new_loc, new_loc_piece = loc_helper.at(0, -2, self)
                if new_loc is not None and new_loc_piece is None:
                    new_locations.append(new_loc)
            # take right!
            new_loc, new_loc_piece = loc_helper.at(+1, -1, self)
            if new_loc is not None and new_loc_piece is not None and piece_color(new_loc_piece) == Board.WHITE:
                new_locations.append(new_loc)
            # take left!
            new_loc, new_loc_piece = loc_helper.at(-1, -1, self)
            if new_loc is not None and new_loc_piece is not None and piece_color(new_loc_piece) == Board.WHITE:
                new_locations.append(new_loc)

        return new_locations

    def knight_moves(self, piece, loc):
        loc_helper = LocationHelper(loc)
        my_color = piece_color(piece)
        new_locations = []

        potential_offsets = (
            (+2, +1),
            (+1, +2),
            (-2, -1),
            (-1, - 2),
            (+2, -1),
            (+1, -2),
            (-2, +1),
            (-1, +2),
        )

        for offset_col, offset_row in potential_offsets:
            new_loc, new_loc_piece = loc_helper.at(
                offset_col, offset_row, self)
            # if empty or opponent
            if new_loc is not None and (new_loc_piece is None or piece_color(new_loc_piece) != my_color):
                new_locations.append(new_loc)

        return new_locations

    def in_check(self, color):
        king_piece = white_color_of("k") if color == Board.WHITE else black_color_of("k")
        king_loc = self.location_of(king_piece)
        for piece in self.pieces():
            piece_loc = self.location_of(piece)
            if piece_color(piece) != color:
                if king_loc in self.possible_moves(piece_loc):
                    # print("Check!")
                    return True
        return False

    def check_mate(self, color):
        for piece in self.pieces():
            if piece_color(piece) == color:
                piece_location = self.location_of(piece)
                for new_location in self.possible_moves(piece_location):
                    try:
                        new_board = self.move_piece(piece_location, new_location)
                    except:
                        # cannot move because in check
                        pass
                    else:
                        # move is allowed and no longer in check
                        return False
        return True

    def castle(self, piece, loc):
        if piece_color(piece) == Board.WHITE and (self.white_can_castle_left or self.white_can_castle_right):
            pass
        elif piece_color(piece) == Board.BLACK and (self.black_can_castle_left or self.black_can_castle_right):
            pass
        else:
            return []

        col_row = loc_to_col_row(loc)
        assert col_row[1] in (0, 7)
        assert col_row[0] == 4
        castle_vals = [0, 0, 0, 0]

        if piece_color(piece) == Board.WHITE:
            if self.white_can_castle_left:
                if self.piece_at("a1") == white_color_of("r1") and \
                   self.piece_at("b1") is None and \
                   self.piece_at("c1") is None and \
                   self.piece_at("d1") is None:
                    castle_vals[1] = -2
            if self.white_can_castle_right:
                if self.piece_at("h1") == white_color_of("r2") and \
                   self.piece_at("g1") is None and \
                   self.piece_at("f1") is None:
                    castle_vals[0] = 2
        else:
            if self.black_can_castle_left:
                if self.piece_at("a8") == black_color_of("r1") and \
                   self.piece_at("b8") is None and \
                   self.piece_at("c8") is None and \
                   self.piece_at("d8") is None:
                    castle_vals[3] = -2
            if self.black_can_castle_right:
                if self.piece_at("h8") == black_color_of("r2") and \
                   self.piece_at("g8") is None and \
                   self.piece_at("f8") is None:
                    castle_vals[2] = 2

        new_positions = []
        for n in castle_vals:
            if n != 0:
                new_positions.append([col_row[0]+n, col_row[1]])

        new_locs = [col_row_to_loc(col_row) for col_row in new_positions]
        return new_locs

    def possible_moves(self, loc):
        piece = self.piece_at(loc)
        new_locations = []
        piece_clr = piece_color(self.piece_at(loc))

        # bishop
        if piece in bishops:
            new_locations.extend(self.diagonal_moves(piece, loc, 8))

        # pawn
        if piece in pawns:
            new_locations.extend(self.pawn_moves(piece, loc))

        # queen
        if piece in queens:
            new_locations.extend(self.diagonal_moves(piece, loc, 8))
            new_locations.extend(self.cross_moves(piece, loc, 8))

        # king
        if piece in kings:
            new_locations.extend(self.diagonal_moves(piece, loc, 2))
            new_locations.extend(self.cross_moves(piece, loc, 2))
            new_locations.extend(self.castle(piece, loc))

        # rook
        if piece in rooks:
            new_locations.extend(self.cross_moves(piece, loc, 8))

        # knight
        if piece in knights:
            new_locations.extend(self.knight_moves(piece, loc))

        return new_locations

    def duplicate(self):
        new_board = Board()
        new_board.positions = [[piece for piece in sub_array]
                               for sub_array in self.positions]
        new_board.piece_locations = None
        new_board.white_can_castle_right = self.white_can_castle_right
        new_board.black_can_castle_right = self.black_can_castle_right
        new_board.white_can_castle_left = self.white_can_castle_left
        new_board.black_can_castle_left = self.black_can_castle_left
        return new_board

    def move_piece(self, old_loc, new_loc):
        # creates a new board with the piece from the old loc to a new loc
        new_board = self.duplicate()
        piece = self.piece_at(old_loc)
        col_row_old = loc_to_col_row(old_loc)
        col_row_new = loc_to_col_row(new_loc)
        rook = ''
        rook_new = ''
        rook_old = ''

        possible_new_locs = self.possible_moves(old_loc)
        piece_clr = piece_color(piece)

        if new_loc in possible_new_locs:
            new_board.set_piece_at(self.piece_at(old_loc), new_loc)
            new_board.set_piece_at(None, old_loc)

            if piece == "r1":
                new_board.white_can_castle_left = False
            elif piece == "r2":
                new_board.white_can_castle_right = False
            if piece == "R1":
                new_board.black_can_castle_left = False
            if piece == "R2":
                new_board.black_can_castle_right = False

            if piece in ['k', 'K']:
                if piece == "k":
                    new_board.white_can_castle_left = False
                    new_board.white_can_castle_right = False
                if piece == "K":
                    new_board.black_can_castle_left = False
                    new_board.black_can_castle_right = False

                cols_moved = col_row_new[0]-col_row_old[0]
                if cols_moved == 2:
                    if piece.islower():
                        rook = 'r2'
                        rook_old = 'h1'
                        rook_new = 'f1'
                    else:
                        rook = 'R2'
                        rook_old = 'h8'
                        rook_new = 'f8'

                elif cols_moved == -2:
                    if piece.islower():
                        rook = 'r1'
                        rook_old = 'a1'
                        rook_new = 'd1'
                    else:
                        rook = 'R1'
                        rook_old = 'a8'
                        rook_new = 'd8'

                if abs(cols_moved) > 1:
                    new_board.set_piece_at(rook, rook_new)
                    new_board.set_piece_at(None, rook_old)

            if new_board.in_check(piece_clr):
                raise Exception("Invalid - cannot move into check")

            return new_board

        else:
            raise Exception("Invalid")
