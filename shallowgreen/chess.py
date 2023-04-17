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
    elif piece in (bishops or knights):
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


def piece_is_white(piece):
    return piece[0].islower()


def piece_color(piece):
    return "white" if piece_is_white(piece) else "black"


class Board(object):

    def find_locations(self):
        self.piece_locations = {}
        for i, row in enumerate(self.positions):
            for j, piece in enumerate(row):
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
        iswhite = piece_is_white(loc)
        for piece in self.pieces():
            if loc in self.possible_moves(self.location_of(piece)):
                if piece_is_white(piece) is not iswhite:
                    pieces_guarding -= 1
                else:
                    pieces_guarding += 1

        if pieces_guarding > 0:
            return iswhite
        elif pieces_guarding < 0:
            return not iswhite
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

    def is_white(self, loc):
        piece = self.piece_at(loc)
        return piece_is_white(piece) if piece is not None else None

    def get_material(self):
        cur_material = 0
        for sub_array in self.positions:
            for piece in sub_array:
                if piece != None:
                    if piece_is_white(piece):
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

        space = 0
        risked = 0
        for piece in self.pieces():
            piece_loc = self.location_of(piece)
            controlling = self.controlling_side(piece_loc)
            if piece is not None:
                if controlling:
                    if piece_is_white(piece_loc) is False:
                        risked -= material(piece)
                elif controlling is False:
                    if piece_is_white(piece):
                        risked += material(piece)
            else:
                if controlling:
                    space += 1
                elif controlling is False:
                    space -= 1
        return space, risked

    def specific_space(self, locs):
        """
        Returns same thing as get_space(), but instead of entire board, only calculates the space of specific locations
        """

        space = 0
        risked = 0
        for square in locs:
            piece = self.piece_at(square)
            controlling = self.controlling_side(square)
            if piece is not None:
                if controlling:
                    if piece_is_white(square) is False:
                        risked -= material(piece)
                elif controlling is False:
                    if piece_is_white(square):
                        risked += material(piece)
            else:
                if controlling:
                    space += 1
                elif controlling is False:
                    space -= 1
        return space, risked

    def compute_score(self, material, safety, space, risk):
        score = 0.0
        print(self)
        print('material is', material)
        print('safety is', safety)
        print('space is', space)
        print('risk is', risk)
        score += material * 0.8
        score += safety
        score += space * 0.95
        score += risk * 0.5
        return score

    def score(self):
        return self.compute_score(
            self.get_material(),
            self.get_safety(),
            self.get_space()[0],
            self.get_space()[1]
        )

    def computer_turn(self, is_white=False):
        best_score = None
        best_move = ''
        best_old_loc = ''
        cur_score = 0
        pieces = self.pieces()

        for piece in pieces:
            old_location = self.location_of(piece)
            if piece_is_white(piece) is is_white:
                for move in self.possible_moves(old_location):
                    new_board = self.move_piece(old_location, move)
                    cur_score = new_board.score()
                    print("scoring", old_location, "to",
                          move, "score is", cur_score)
                    if (is_white is True and (best_score is None or cur_score > best_score)) or \
                            (is_white is False and (best_score is None or cur_score < best_score)):
                        best_score = cur_score
                        best_old_loc = old_location
                        best_move = move

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
        is_white = self.is_white(loc)

        if is_white:  # white moves
            new_loc, new_loc_piece = loc_helper.at(0, 1, self)
            if new_loc is not None and new_loc_piece is None:
                new_locations.append(new_loc)
            if cur_row == 1:
                new_loc, new_loc_piece = loc_helper.at(0, 2, self)
                if new_loc is not None and new_loc_piece is None:
                    new_locations.append(new_loc)
            # take right!
            new_loc, new_loc_piece = loc_helper.at(+1, +1, self)
            if new_loc is not None and new_loc_piece is not None and piece_is_white(new_loc_piece) is False:
                new_locations.append(new_loc)
            # take left!
            new_loc, new_loc_piece = loc_helper.at(-1, +1, self)
            if new_loc is not None and new_loc_piece is not None and piece_is_white(new_loc_piece) is False:
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
            if new_loc is not None and new_loc_piece is not None and piece_is_white(new_loc_piece):
                new_locations.append(new_loc)
            # take left!
            new_loc, new_loc_piece = loc_helper.at(-1, -1, self)
            if new_loc is not None and new_loc_piece is not None and piece_is_white(new_loc_piece):
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

    def castle(self, piece, loc):
        col_row = loc_to_col_row(loc)

        castle_vals = [0, 0, 0, 0]
        if self.white_can_castle_left:
            castle_vals[1] = -2
        if self.white_can_castle_right:
            castle_vals[0] = 2
        if self.black_can_castle_left:
            castle_vals[3] = -2
        if self.black_can_castle_right:
            castle_vals[2] = 2

        if piece_is_white(piece) is True:
            castle_vals[3] = 0
            castle_vals[2] = 0
        else:
            castle_vals[1] = 0
            castle_vals[0] = 0

        new_positions = []
        for n in castle_vals:
            if n != 0:
                new_positions.append([col_row[0]+n, col_row[1]])

        new_locs = [col_row_to_loc(col_row) for col_row in new_positions]
        new_locs = [new_loc for new_loc in new_locs if
                    self.piece_at(new_loc) is None or self.is_white(new_loc) != self.is_white(loc)]
        return new_locs

    def possible_moves(self, loc):
        piece = self.piece_at(loc)
        new_locations = []

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

    def move_piece(self, old_loc, new_loc):
        # creates a new board with the piece from the old loc to a new loc
        new_board = Board()
        new_board.positions = [[piece for piece in sub_array]
                               for sub_array in self.positions]
        piece = self.piece_at(old_loc)
        col_row_old = loc_to_col_row(old_loc)
        col_row_new = loc_to_col_row(new_loc)
        rook = ''
        rook_new = ''
        rook_old = ''

        possible_new_locs = self.possible_moves(old_loc)
        if new_loc in possible_new_locs:
            new_board.set_piece_at(self.piece_at(old_loc), new_loc)
            new_board.set_piece_at(None, old_loc)
            if piece == "r1":
                self.white_can_castle_left = False
            elif piece == "r2":
                self.white_can_castle_right = False
            if piece == "R1":
                self.black_can_castle_left = False
            if piece == "R2":
                self.black_can_castle_right = False

            if piece in ['k', 'K']:
                if piece == "k":
                    self.white_can_castle_left = False
                    self.white_can_castle_right = False
                if piece == "K":
                    self.black_can_castle_left = False
                    self.black_can_castle_right = False

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
                    self.set_piece_at(rook, rook_new)
                    self.set_piece_at(None, rook_old)
            return new_board
        else:
            raise Exception("Invalid")
