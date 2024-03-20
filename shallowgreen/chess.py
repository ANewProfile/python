DEBUG_MOVE = False


def loc_to_col_row(loc):
    loc = loc.lower()
    return ord(loc[0])-ord('a'), int(loc[1])-1


def col_row_to_loc(pos):
    return "".join([chr(ord('a') + pos[0]), str(pos[1]+1)])


def loc_is_white(loc):
    col, row = loc_to_col_row(loc)
    return (col%2 == 0 and row%2 == 1) or \
           (col%2 == 1 and row%2 == 0)

def loc_is_black(loc):
    col, row = loc_to_col_row(loc)
    return (col%2 == 1 and row%2 == 1) or \
           (col%2 == 0 and row%2 == 0)


PAWNS = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
         'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8')
ROOKS = ('r1', 'r2', 'R1', 'R2')
BISHOPS = ('b1', 'b2', 'B1', 'B2')
KNIGHTS = ('k1', 'k2', 'K1', 'K2')
QUEENS = ('q', 'Q')
KINGS = ('k', 'K')


class GameOverException(Exception):
    pass


class InvalidMoveException(Exception):
    pass


def material(piece):
    if piece in PAWNS:
        return 1
    elif piece in ROOKS:
        return 5
    elif piece in BISHOPS or piece in KNIGHTS:
        return 3
    elif piece in QUEENS:
        return 9
    else:
        return 0


def king_material():
    return 10000


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
            return [new_loc, board.piece_at_col_row(new_col, new_row)]
        else:
            return [None, None]


def piece_color(piece):
    if piece == "" or piece is None:
        return None
    # faster than regex or islower
    return Board.WHITE if piece[0] in 'abcdefghijklmnopqrstuvwxyz' else Board.BLACK


def white_piece(piece):
    return piece.lower()


def black_piece(piece):
    return piece.upper()


def get_piece(name, color):
    return white_piece(name) if color == Board.WHITE else black_piece(name)


def rows_to_opp_end(piece, loc):
    col, row = loc_to_col_row(loc)
    if piece_color(piece) is Board.WHITE:
        return 7-row
    else:
        return row


class Board(object):
    WHITE = "white"
    BLACK = "black"

    def find_locations(self):
        self.__piece_locations = {}
        for i, array in enumerate(self.positions):
            for j, piece in enumerate(array):
                if piece is not None:
                    row = 7 - i
                    col = j
                    loc = col_row_to_loc([col, row])
                    self.__piece_locations[piece] = loc

    def location_of(self, piece):
        if self.__piece_locations is None:
            self.find_locations()
        if piece not in self.__piece_locations:
            return None
        return self.__piece_locations[piece]

    def pieces(self):
        if self.__piece_locations is None:
            self.find_locations()
        return self.__piece_locations.keys()

    def piece_and_locations(self):
        if self.__piece_locations is None:
            self.find_locations()
        return self.__piece_locations.items()

    def piece_at_col_row(self, col, row):
        if col >= 0 and col < 8 and \
           row >= 0 and row < 8:
            return self.positions[7-row][col]
        return None

    def piece_at(self, loc):
        col, row = loc_to_col_row(loc)
        return self.piece_at_col_row(col, row)

    def set_piece_at(self, piece, loc):
        assert self.__allow_set_piece is True
        pos = loc_to_col_row(loc)
        self.positions[7-pos[1]][pos[0]] = piece
        self.__piece_locations = None

    def assign_controls(self, just_moved_color):
        self.__controlling[just_moved_color] = {}

        for piece, piece_loc in self.piece_and_locations():
            piece_clr = piece_color(piece)
            opp_color_of_piece = Board.WHITE if piece_clr == Board.BLACK else Board.BLACK
            piece_attacked_by_opp = self.attacked_by(piece_loc, opp_color_of_piece)

	    # a piece controlled by opp side that is about to move cannot
	    # control other spaces - it's at risk. note that it's not the same
	    # as checking if a piece is controlled by its own side.
            if piece_attacked_by_opp and just_moved_color != opp_color_of_piece:
                # print("%s cannot control anything" % piece)
                continue

            locs_to_check = self.possible_moves(piece_loc) + self.blocked_at(piece_loc)
            for next_move_loc in set(locs_to_check):
                # pawn cannot control same column
                if piece in PAWNS and piece_loc[0] == next_move_loc[0]:
                    continue
                if next_move_loc not in self.__controlling[just_moved_color]:
                    self.__controlling[just_moved_color][next_move_loc] = 0
                if piece_clr == Board.BLACK:
                    self.__controlling[just_moved_color][next_move_loc] -= 1
                else:
                    self.__controlling[just_moved_color][next_move_loc] += 1

    def controlling_side(self, loc, just_moved_color):
        if self.__controlling[just_moved_color] is None:
            self.assign_controls(just_moved_color)
        if loc in self.__controlling[just_moved_color]:
            pieces_guarding = self.__controlling[just_moved_color][loc]
        else:
            pieces_guarding = 0

        if pieces_guarding > 0:
            return Board.WHITE
        elif pieces_guarding < 0:
            return Board.BLACK
        else:
            return None

    def attacked_by(self, loc, color):
        """
        Returns True if specified location can be taken by a piece of the specified color.
        """

        cache_key = (loc, color)
        if cache_key in self.__attacked_by:
            return self.__attacked_by[cache_key]

        for piece, piece_loc in self.piece_and_locations():
            if piece_color(piece) == color:
                if loc in self.possible_moves(piece_loc, include_castle=False) or \
                   loc in self.blocked_at(piece_loc):
                    # pawn cannot attack the square in front of it
                    if piece not in PAWNS or piece_loc[0] != loc[0]:
                        self.__attacked_by[cache_key] = True
                        return True

        self.__attacked_by[cache_key] = False
        return False

    def __str__(self):
        return "\n".join(
            [" | ".join(["  " if piece is None else "%2s" % (piece)
                        for piece in sub_array]) for sub_array in self.positions]
        )

    def __set_initial_positions(self):
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

    def duplicate(self):
        new_board = Board(empty=True)
        new_board.positions = [[piece for piece in sub_array]
                               for sub_array in self.positions]
        new_board.white_can_castle_right = self.white_can_castle_right
        new_board.black_can_castle_right = self.black_can_castle_right
        new_board.white_can_castle_left = self.white_can_castle_left
        new_board.black_can_castle_left = self.black_can_castle_left
        return new_board

    def __init__(self, empty=False):
        self.positions = [[None for i in range(8)] for j in range(8)]
        self.__allow_set_piece = False

        # data structures for caching
        self.__piece_locations = None
        self.__moves_non_castle = {}
        self.__moves_castle = {}
        self.__moves_blocked = {}
        self.__controlling = { Board.WHITE: None, Board.BLACK: None }
        self.__attacked_by = {}
        self.__check_mate = {}

        self.white_can_castle_right = True
        self.black_can_castle_right = True
        self.white_can_castle_left = True
        self.black_can_castle_left = True

        if empty is False:
            self.__allow_set_piece = True
            self.__set_initial_positions()
            self.__allow_set_piece = False

    def key(self):
        return "".join(["".join([piece if piece is not None else "_" for piece in sub_array])
                       for sub_array in self.positions])

    def piece_locations(self):
        if self.__piece_locations is None:
            self.find_locations()
        return {k:v for k,v in self.__piece_locations.items()}

    @staticmethod
    def custom_board(piece_locations):
        board = Board(empty=True)
        board.__allow_set_piece = True
        for piece, location in piece_locations.items():
            board.set_piece_at(piece, location)
        board.__allow_set_piece = False
        return board

    def loc_piece_color(self, loc):
        piece = self.piece_at(loc)
        return piece_color(piece)

    def diagonal_moves(self, piece, loc, total_range):
        loc_helper = LocationHelper(loc)
        cont = [True, True, True, True]
        new_locations = []
        blocking_locations = []
        piece_clr = piece_color(piece)

        for i in range(1, total_range):
            if cont[0] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, -i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[0] = False

            if cont[1] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, +i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[1] = False

            if cont[2] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, -i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[2] = False

            if cont[3] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, +i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[3] = False

        return new_locations, blocking_locations

    def cross_moves(self, piece, loc, total_range):
        loc_helper = LocationHelper(loc)
        cont = [True, True, True, True]
        new_locations = []
        blocking_locations = []
        piece_clr = piece_color(piece)

        for i in range(1, total_range):
            if cont[0] is True:
                new_loc, new_loc_piece = loc_helper.at(0, -i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[0] = False

            if cont[1] is True:
                new_loc, new_loc_piece = loc_helper.at(0, +i, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[1] = False

            if cont[2] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, 0, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[2] = False

            if cont[3] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, 0, self)
                if new_loc:  # location is valid
                    # if empty or opponent
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_clr:
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        blocking_locations.append(new_loc)
                        cont[3] = False

        return new_locations, blocking_locations

    def pawn_moves(self, loc):
        loc_helper = LocationHelper(loc)
        _, cur_row = loc_to_col_row(loc)
        new_locations = []
        blocking_locations = []
        piece_clr = self.loc_piece_color(loc)

        if piece_clr == Board.WHITE:  # white moves

            # move up one
            loc_in_front, piece_in_front = loc_helper.at(0, 1, self)
            if loc_in_front is not None and piece_in_front is None:
                new_locations.append(loc_in_front)

            # move up two if nothing blocking it
            if loc_in_front is not None and cur_row == 1 and piece_in_front is None:
                new_loc, new_loc_piece = loc_helper.at(0, 2, self)
                if new_loc is not None and new_loc_piece is None:
                    new_locations.append(new_loc)

            # take right!
            new_loc, new_loc_piece = loc_helper.at(+1, +1, self)
            if new_loc is not None:
               if new_loc_piece is not None and piece_color(new_loc_piece) == Board.BLACK:
                  new_locations.append(new_loc)
               else:
                  blocking_locations.append(new_loc)

            # take left!
            new_loc, new_loc_piece = loc_helper.at(-1, +1, self)
            if new_loc is not None:
               if new_loc_piece is not None and piece_color(new_loc_piece) == Board.BLACK:
                  new_locations.append(new_loc)
               else:
                  blocking_locations.append(new_loc)

        else:  # black moves

            # move down one
            loc_in_front, piece_in_front = loc_helper.at(0, -1, self)
            if loc_in_front is not None and piece_in_front is None:
                new_locations.append(loc_in_front)

            # move down two if nothing blocking it
            if loc_in_front is not None and cur_row == 6 and piece_in_front is None:
                new_loc, new_loc_piece = loc_helper.at(0, -2, self)
                if new_loc is not None and new_loc_piece is None:
                    new_locations.append(new_loc)

            # take right!
            new_loc, new_loc_piece = loc_helper.at(+1, -1, self)
            if new_loc is not None:
               if new_loc_piece is not None and piece_color(new_loc_piece) == Board.WHITE:
                  new_locations.append(new_loc)
               else:
                  blocking_locations.append(new_loc)

            # take left!
            new_loc, new_loc_piece = loc_helper.at(-1, -1, self)
            if new_loc is not None:
               if new_loc_piece is not None and piece_color(new_loc_piece) == Board.WHITE:
                  new_locations.append(new_loc)
               else:
                  blocking_locations.append(new_loc)

        return new_locations, blocking_locations

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
        opp_color = Board.WHITE if color == Board.BLACK else Board.BLACK
        king_piece = get_piece('k', color)
        king_loc = self.location_of(king_piece)

        if self.attacked_by(king_loc, opp_color):
            return True
        return False

    def check_mate(self, color):
        if color in self.__check_mate:
            return self.__check_mate[color]

        if self.in_check(color) is False:
            self.__check_mate[color] = False
            return False

        for piece, piece_location in self.piece_and_locations():
            if piece_color(piece) == color:
                for new_location in self.possible_moves(piece_location):
                    try:
                        new_board = self.move_piece(
                            piece_location, new_location)
                    except InvalidMoveException as e:
                        # cannot move because in check
                        pass
                    else:
                        # move is allowed and no longer in check
                        self.__check_mate[color] = False
                        return False

        self.__check_mate[color] = True
        return True

    def castle(self, piece, loc):

        if piece not in KINGS or loc not in ["e1", "e8"]:
            return []

        if piece_color(piece) == Board.BLACK and \
           self.black_can_castle_left and \
           self.piece_at("a8") == black_piece("r1") and \
           self.piece_at("b8") is None and \
           self.piece_at("c8") is None and \
           self.piece_at("d8") is None:
            pass

        elif piece_color(piece) == Board.BLACK and \
             self.black_can_castle_right and \
             self.piece_at("h8") == black_piece("r2") and \
             self.piece_at("g8") is None and \
             self.piece_at("f8") is None:
            pass

        elif piece_color(piece) == Board.WHITE and \
             self.white_can_castle_left and \
             self.piece_at("a1") == white_piece("r1") and \
             self.piece_at("b1") is None and \
             self.piece_at("c1") is None and \
             self.piece_at("d1") is None:
            pass

        elif piece_color(piece) == Board.WHITE and \
             self.white_can_castle_right and \
             self.piece_at("h1") == white_piece("r2") and \
             self.piece_at("g1") is None and \
             self.piece_at("f1") is None:
            pass

        else:
            return []

        col_row = loc_to_col_row(loc)
        assert col_row[1] in (0, 7)
        assert col_row[0] == 4
        castle_vals = [0, 0, 0, 0]

        if piece_color(piece) == Board.WHITE:
            if self.white_can_castle_left and \
               not self.attacked_by('d1', Board.BLACK) and \
               not self.attacked_by('c1', Board.BLACK) and \
               not self.attacked_by('b1', Board.BLACK) and \
               not self.attacked_by('e1', Board.BLACK):
                castle_vals[1] = -2

            if self.white_can_castle_right and \
               not self.attacked_by('f1', Board.BLACK) and \
               not self.attacked_by('g1', Board.BLACK) and \
               not self.attacked_by('e1', Board.BLACK):
                castle_vals[0] = 2

        else:  # black castle

            # can't castle through or from check - black
            if self.black_can_castle_left and \
               not self.attacked_by('d8', Board.WHITE) and \
               not self.attacked_by('c8', Board.WHITE) and \
               not self.attacked_by('b8', Board.WHITE) and \
               not self.attacked_by('e8', Board.WHITE):
                castle_vals[3] = -2

            if self.black_can_castle_right and \
               not self.attacked_by('f8', Board.WHITE) and \
               not self.attacked_by('g8', Board.WHITE) and \
               not self.attacked_by('e8', Board.WHITE):
                castle_vals[2] = 2

        new_positions = []
        for n in castle_vals:
            if n != 0:
                new_positions.append([col_row[0]+n, col_row[1]])
        new_locs = [col_row_to_loc(col_row) for col_row in new_positions]
        return new_locs

    def blocked_at(self, loc):
        if loc in self.__moves_blocked:
            return self.__moves_blocked[loc]

        self.possible_moves(loc)

        if loc in self.__moves_blocked:
            return self.__moves_blocked[loc]
        return []

    def compute_moves(self, loc):
        piece = self.piece_at(loc)
        new_locations = []
        blocking_locations = []
        castled_locations = []

        # bishop
        if piece in BISHOPS:
            moves, blocking = self.diagonal_moves(piece, loc, 8)
            new_locations.extend(moves)
            blocking_locations.extend(blocking)

        # pawn
        if piece in PAWNS:
            moves, blocking = self.pawn_moves(loc)
            new_locations.extend(moves)
            blocking_locations.extend(blocking)

        # queen
        if piece in QUEENS:
            moves, blocking = self.diagonal_moves(piece, loc, 8)
            new_locations.extend(moves)
            blocking_locations.extend(blocking)

            moves, blocking = self.cross_moves(piece, loc, 8)
            new_locations.extend(moves)
            blocking_locations.extend(blocking)

        # king
        if piece in KINGS:
            moves, blocking = self.diagonal_moves(piece, loc, 2)
            new_locations.extend(moves)
            blocking_locations.extend(blocking)

            moves, blocking = self.cross_moves(piece, loc, 2)
            new_locations.extend(moves)
            blocking_locations.extend(blocking)

            castled_locations.extend(self.castle(piece, loc))

        # rook
        if piece in ROOKS:
            moves, blocking = self.cross_moves(piece, loc, 8)
            new_locations.extend(moves)
            blocking_locations.extend(blocking)

        # knight
        if piece in KNIGHTS:
            new_locations.extend(self.knight_moves(piece, loc))

        # tuples faster than lists
        return tuple(new_locations), tuple(castled_locations), tuple(blocking_locations)

    def possible_moves(self, loc, include_castle=True):
        if loc not in self.__moves_non_castle:
            moves_non_castle, moves_castle, moves_blocked = self.compute_moves(loc)
            self.__moves_non_castle[loc] = moves_non_castle
            self.__moves_castle[loc] = moves_castle
            self.__moves_blocked[loc] = moves_blocked

        if include_castle:
            return self.__moves_castle[loc]+self.__moves_non_castle[loc]
        return self.__moves_non_castle[loc]

    def move_piece(self, old_loc, new_loc, promotion=None):
        # creates a new board with the piece from the old loc to a new loc
        new_board = self.duplicate()
        new_board.__allow_set_piece = True

        piece = self.piece_at(old_loc)
        col_row_old = loc_to_col_row(old_loc)
        col_row_new = loc_to_col_row(new_loc)
        rook = ''
        rook_new = ''
        rook_old = ''

        possible_new_locs = self.possible_moves(old_loc)
        piece_clr = piece_color(piece)
        if promotion is None:
            promotion = get_piece('q', piece_clr)

        if new_loc not in possible_new_locs:
            raise InvalidMoveException("Invalid move")

        new_board.set_piece_at(self.piece_at(old_loc), new_loc)
        new_board.set_piece_at(None, old_loc)

        if piece == white_piece('r1'):
            new_board.white_can_castle_left = False
        elif piece == white_piece('r2'):
            new_board.white_can_castle_right = False
        if piece == black_piece('R1'):
            new_board.black_can_castle_left = False
        if piece == black_piece('R2'):
            new_board.black_can_castle_right = False

        if piece in KINGS:
            if piece == white_piece('k'):
                new_board.white_can_castle_left = False
                new_board.white_can_castle_right = False
            if piece == black_piece('K'):
                new_board.black_can_castle_left = False
                new_board.black_can_castle_right = False

            cols_moved = col_row_new[0]-col_row_old[0]
            if cols_moved == 2:
                if piece.islower():
                    rook = white_piece('r2')
                    rook_old = 'h1'
                    rook_new = 'f1'
                else:
                    rook = black_piece('R2')
                    rook_old = 'h8'
                    rook_new = 'f8'

            elif cols_moved == -2:
                if piece.islower():
                    rook = white_piece('r1')
                    rook_old = 'a1'
                    rook_new = 'd1'
                else:
                    rook = black_piece('R1')
                    rook_old = 'a8'
                    rook_new = 'd8'

            if abs(cols_moved) > 1:
                new_board.set_piece_at(rook, rook_new)
                new_board.set_piece_at(None, rook_old)

        if new_board.in_check(piece_clr):
            raise InvalidMoveException("Invalid - cannot move into check")

        if piece in PAWNS and col_row_new[1] in (0, 7) and promotion is not None:
            assert piece_color(piece) == piece_color(promotion)
            new_board.set_piece_at(promotion, new_loc)
            new_board.set_piece_at(None, old_loc)

        new_board.__allow_set_piece = False
        return new_board


class BoardAnalyzer(object):

    def __init__(self, board):
        self.board = board

    def score(self, just_moved_color):
        """
        Return a numeric score
        """
        raise Exception("Implement me")


class Move(object):
    """
    Represents a move, which is an actual move (old_location, new_location)
    tuple, a resulting board, and the side that moved.
    """

    def __init__(self, moved_piece, move, new_board, just_moved_color):
        self.moved_piece = moved_piece
        self.move = move
        self.new_board = new_board
        self.just_moved_color = just_moved_color

    @property
    def next_move_color(self):
        return Board.WHITE if self.just_moved_color == Board.BLACK else Board.BLACK
