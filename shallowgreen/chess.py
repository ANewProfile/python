def loc_to_col_row(loc):
    return ord(loc[0])-ord('a'), int(loc[1])-1


def col_row_to_loc(pos):
    return "".join([chr(ord('a') + pos[0]), str(pos[1]+1)])


class LocationHelper(object):

    def __init__(self, loc):
        self.loc = loc
        self.col_row = loc_to_col_row(loc)

    def at(self, col_offset, row_offset, board):
        # returns (loc, piece) tuple
        # if offset moves position off the board, returns (None, None)

        new_col = self.col_row[0] + col_offset
        new_row = self.col_row[1] + row_offset
        if new_col >= 0 and new_col < 8 and new_row >= 0 and new_col < 8:
            new_loc = col_row_to_loc([new_col, new_row])
            return [new_loc, board.piece_at(new_loc)]
        else:
            return [None, None]


class Piece(object):

    def __init__(self, piece):
        self.piece = piece


def piece_is_white(piece):
    return piece[0].islower()


def piece_color(piece):
    return "white" if piece_is_white(piece) else "black"


class Board(object):

    def piece_at(self, loc):
        pos = loc_to_col_row(loc)
        return self.positions[7-pos[1]][pos[0]]

    def set_piece_at(self, piece, loc):
        pos = loc_to_col_row(loc)
        self.positions[7-pos[1]][pos[0]] = piece

    def __str__(self):
        return "\n".join(
            [" | ".join(["  " if p is None else "%2s" % (p) for p in sub_array]) for sub_array in self.positions]
        )

    def __init__(self):
        self.positions = [[None for i in range(8)] for j in range(8)]

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
        n = self.piece_at(loc)
        return piece_is_white(n) if n is not None else None

    def diagonal_moves(self, piece, loc, total_range):

        loc_helper = LocationHelper(loc)
        cont = [True, True, True, True]
        new_locations = []

        for i in range(1, total_range):
            if cont[0] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, -i, self)
                if new_loc:  # location is valid
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[0] = False

            if cont[1] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, +i, self)
                if new_loc:  # location is valid
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[1] = False

            if cont[2] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, -i, self)
                if new_loc:  # location is valid
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[2] = False

            if cont[3] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, +i, self)
                if new_loc:  # location is valid
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
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
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[0] = False

            if cont[1] is True:
                new_loc, new_loc_piece = loc_helper.at(0, +i, self)
                if new_loc:  # location is valid
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[1] = False

            if cont[2] is True:
                new_loc, new_loc_piece = loc_helper.at(+i, 0, self)
                if new_loc:  # location is valid
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[2] = False

            if cont[3] is True:
                new_loc, new_loc_piece = loc_helper.at(-i, 0, self)
                if new_loc:  # location is valid
                    if new_loc_piece is None or piece_color(new_loc_piece) != piece_color(piece):  # if empty or opponent
                        new_locations.append(new_loc)
                    if new_loc_piece:  # blocked, don't continue
                        cont[3] = False

        return new_locations

    def pawn_moves(self, piece, loc):
        cur_pos = loc_to_col_row(loc)
        new_positions = []
        
        if self.piece_at(col_row_to_loc([cur_pos[0], cur_pos[1]+1])) == None and self.is_white(loc):
            new_positions.append([cur_pos[0], cur_pos[1]+1])
        elif self.piece_at(col_row_to_loc([cur_pos[0], cur_pos[1]-1])) == None and self.is_white(loc) is False:
            new_positions.append([cur_pos[0], cur_pos[1]-1])

        if cur_pos[1] == 1 and self.is_white(loc) and self.piece_at(col_row_to_loc([cur_pos[0], cur_pos[1]+2])) == None:
            new_positions.append([cur_pos[0], cur_pos[1]+2])
        elif cur_pos[1] == 6 and self.is_white(loc) is False and \
             self.piece_at(col_row_to_loc([cur_pos[0], cur_pos[1]-2])) == None:
            new_positions.append([cur_pos[0], cur_pos[1]-2])

        if (n := self.is_white(col_row_to_loc([cur_pos[0]+1, cur_pos[1]+1]))) == False:
            if (y := self.is_white(loc)):
                new_positions.append([cur_pos[0]+1, cur_pos[1]+1])
            else:
                pass
        else:
            pass

        if (n := self.is_white(col_row_to_loc([cur_pos[0]-1, cur_pos[1]+1]))) == False:
            if (y := self.is_white(loc)):
                new_positions.append([cur_pos[0]-1, cur_pos[1]+1])
            else:
                pass
        else:
            pass

        # 
        if (n := self.is_white(col_row_to_loc([cur_pos[0]+1, cur_pos[1]-1]))):
            if (y := self.is_white(loc)) == False:
                new_positions.append([cur_pos[0]+1, cur_pos[1]-1])
            else:
                pass
        else:
            pass
        if (n := self.is_white(col_row_to_loc([cur_pos[0]-1, cur_pos[1]-1]))):
            if (y := self.is_white(loc)) == False:
                new_positions.append([cur_pos[0]-1, cur_pos[1]-1])
            else:
                pass
        else:
            pass

        new_positions = [p for p in new_positions
                         if p[0] >= 0 and p[1] >= 0 and p[0] < 8 and p[1] < 8]
        new_locs = [col_row_to_loc(p) for p in new_positions]

        new_locs = [new_loc for new_loc in new_locs if
                    self.piece_at(new_loc) is None or self.is_white(new_loc) != self.is_white(loc)]
        return new_locs

    def knight_moves(self, piece, loc):
        cur_pos = loc_to_col_row(loc)
        new_positions = []

        new_positions.append([cur_pos[0]+2, cur_pos[1]+1])
        new_positions.append([cur_pos[0]+1, cur_pos[1]+2])
        new_positions.append([cur_pos[0]-2, cur_pos[1]-1])
        new_positions.append([cur_pos[0]-1, cur_pos[1]-2])
        new_positions.append([cur_pos[0]+2, cur_pos[1]-1])
        new_positions.append([cur_pos[0]+1, cur_pos[1]-2])
        new_positions.append([cur_pos[0]-2, cur_pos[1]+1])
        new_positions.append([cur_pos[0]-1, cur_pos[1]+2])

        new_positions = [p for p in new_positions
                         if p[0] >= 0 and p[1] >= 0 and p[0] < 8 and p[1] < 8]
        new_locs = [col_row_to_loc(p) for p in new_positions]

        new_locs = [new_loc for new_loc in new_locs if
                    self.piece_at(new_loc) is None or self.is_white(new_loc) != self.is_white(loc)]
        return new_locs

    def possible_moves(self, loc):
        piece = self.piece_at(loc)
        new_locations = []

        # bishop
        if piece in ('b1', 'b2', 'B1', 'B2'):
            new_locations.extend(self.diagonal_moves(piece, loc, 8))

        # pawn
        if piece in ("p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "P1", 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'):
            new_locations.extend(self.pawn_moves(piece, loc))

        # queen
        if piece in ('q', 'Q'):
            new_locations.extend(self.diagonal_moves(piece, loc, 8))
            new_locations.extend(self.cross_moves(piece, loc, 8))

        # king
        if piece in ('k', 'K'):
            new_locations.extend(self.diagonal_moves(piece, loc, 2))
            new_locations.extend(self.cross_moves(piece, loc, 2))

        # rook
        if piece in ('r1', 'r2', 'R1', 'R2'):
            new_locations.extend(self.cross_moves(piece, loc, 8))

        # knight
        if piece in ('k1', 'K1', 'k2', 'K2'):
            new_locations.extend(self.knight_moves(piece, loc))

        return new_locations

    def move_piece(self, old_loc, new_loc):

        # creates a new board with the piece from the old loc to a new loc
        new_board = Board()
        new_board.positions = self.positions

        if new_loc in self.possible_moves(old_loc):
            new_board.set_piece_at(self.piece_at(old_loc), new_loc)
            new_board.set_piece_at(None, old_loc)
            return new_board
        else:
            return "Invalid"
