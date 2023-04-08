def loc_to_position(loc):
    return ord(loc[0])-ord('a'), int(loc[1])-1


def position_to_loc(pos):
    return "".join([chr(ord('a') + pos[0]), str(pos[1]+1)])


class Board(object):

    def piece_at(self, loc):
        pos = loc_to_position(loc)
        print(pos[0], pos[1])
        return self.positions[7-pos[1]][pos[0]]

    def set_piece_at(self, piece, loc):
        pos = loc_to_position(loc)
        self.positions[7-pos[1]][pos[0]] = piece

    def __str__(self):
        return "\n".join([" | ".join(["  " if loc is None else "%2s" % (loc) for loc in sub_array]) for sub_array in self.positions])

    def move_piece(self, old_loc, new_loc):
        piece = piece_at(old_loc)
        new_board = Board()
        new_board.positions = self.positions.copy()
        new_board.set_piece_at(piece, new_loc)
        new_board.set_piece_at(None, old_loc)
        return new_board

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
        return n[0].islower() if n is not None else None

    def possible_moves(self, loc):
        piece = self.piece_at(loc)
        cur_pos = loc_to_position(loc)
        new_positions = []
        boards = []

        # bishop
        if piece in ('b1', 'b2', 'B1', 'B2'):

            cont = [True, True, True, True]
            for i in range(1, 8):
                if cont[0] is True:
                    if self.piece_at(position_to_loc([cur_pos[0]-i, cur_pos[1]-i])) is not None:
                        cont[0] = False
                    else:
                        new_positions.append([cur_pos[0]-i, cur_pos[1]-i])

                if cont[1] is True:
                    if self.piece_at(position_to_loc([cur_pos[0]-i, cur_pos[1]+i])) is not None:
                        cont[1] = False
                    else:
                        new_positions.append([cur_pos[0]-i, cur_pos[1]+i])

                if cont[2] is True:
                    if self.piece_at(position_to_loc([cur_pos[0]+i, cur_pos[1]-i])) is not None:
                        cont[2] = False
                    else:
                        new_positions.append([cur_pos[0]+i, cur_pos[1]-i])
                
                if cont[3] is True:
                    if self.piece_at(position_to_loc([cur_pos[0]+i, cur_pos[1]+i])):
                        cont[3] = False
                    else:
                        new_positions.append([cur_pos[0]+i, cur_pos[1]+i])

        # pawn
        if piece in ("p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "P1", 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'):
            if self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]+1])) == None and self.is_white(loc):
                new_positions.append([cur_pos[0], cur_pos[1]+1])
            elif self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]-1])) == None and self.is_white(loc) is False:
                new_positions.append([cur_pos[0], cur_pos[1]-1])


            if cur_pos[1] == 1 and self.is_white(loc) and self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]+2])) == None:
                new_positions.append([cur_pos[0], cur_pos[1]+2])
            elif cur_pos[1] == 6 and self.is_white(loc) is False and self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]-2])) == None:
                new_positions.append([cur_pos[0], cur_pos[1]-2])
            if (n := self.is_white(position_to_loc([cur_pos[0]+1, cur_pos[1]+1]))) == False:
                if (y := self.is_white(loc)):
                    new_positions.append([cur_pos[0]+1, cur_pos[1]+1])
                else:
                    pass
            else:
                pass
            if (n := self.is_white(position_to_loc([cur_pos[0]-1, cur_pos[1]+1]))) == False:
                if (y := self.is_white(loc)):
                    new_positions.append([cur_pos[0]-1, cur_pos[1]+1])
                else:
                    pass
            else:
                pass

            # 
            if (n := self.is_white(position_to_loc([cur_pos[0]+1, cur_pos[1]-1]))):
                if (y := self.is_white(loc)) == False:
                    new_positions.append([cur_pos[0]+1, cur_pos[1]-1])
                else:
                    pass
            else:
                pass
            if (n := self.is_white(position_to_loc([cur_pos[0]-1, cur_pos[1]-1]))):
                if (y := self.is_white(loc)) == False:
                    new_positions.append([cur_pos[0]-1, cur_pos[1]-1])
                else:
                    pass
            else:
                pass

        # queen
        if piece in ('q', 'Q'):
            cont = [True, True, True, True, True, True, True, True]

            for i in range(1, 8):
                if cont[0] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]-i, cur_pos[1]-i])) is not None:
                        cont[0] = False
                    else:
                        new_positions.append([cur_pos[0]-i, cur_pos[1]-i])
                
                if cont[1] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]-i, cur_pos[1]+i])) is not None:
                        cont[1] = False
                    else:
                        new_positions.append([cur_pos[0]-i, cur_pos[1]+i])
                
                if cont[2] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]+i, cur_pos[1]-i])) is not None:
                        cont[2] == False
                    else:
                        new_positions.append([cur_pos[0]+i, cur_pos[1]-i])
                
                if cont[3] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]+i, cur_pos[1]+i])) is not None:
                        cont[3] = False
                    else:
                        new_positions.append([cur_pos[0]+i, cur_pos[1]+i])

                if cont[4] == True:
                    if self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]+i])) is not None:
                        cont[4] = False
                    else:
                        new_positions.append([cur_pos[0], cur_pos[1]+i])
                
                if cont[5] == True:
                    if self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]-i])) is not None:
                        cont[5] = False
                    else:
                        new_positions.append([cur_pos[0], cur_pos[1]-i])
                
                if cont[6] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]+i, cur_pos[1]])) is not None:
                        cont[6] = False
                    else:
                        new_positions.append([cur_pos[0]+i, cur_pos[1]])
                
                if cont[7] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]-i, cur_pos[1]])):
                        cont[7] = False
                    else:
                        new_positions.append([cur_pos[0]-i, cur_pos[1]])

        # king
        if piece in ('k', 'K'):

            for i in range(1, 8):
                if piece_at(position_to_loc([cur_pos[0]-1, cur_pos[1]-1])) is None:
                    new_positions.append([cur_pos[0]-1, cur_pos[1]-1])

                if piece_at(position_to_loc([cur_pos[0]-1, cur_pos[1]+1])) is None:
                    new_positions.append([cur_pos[0]-1, cur_pos[1]+1])
                
                if piece_at(position_to_loc([cur_pos[0]+1, cur_pos[1]-1])) is None:
                    new_positions.append([cur_pos[0]+1, cur_pos[1]-1])
                
                if piece_at(position_to_loc([cur_pos[0]+1, cur_pos[1]+1])) is None:
                    new_positions.append([cur_pos[0]+1, cur_pos[1]+1])
                
                if piece_at(position_to_loc([cur_pos[0], cur_pos[1]+1])) is None:
                    new_positions.append([cur_pos[0], cur_pos[1]+1])
                
                if piece_at(position_to_loc([cur_pos[0], cur_pos[1]-1])) is None:
                    new_positions.append([cur_pos[0], cur_pos[1]-1])
                
                if piece_at(position_to_loc([cur_pos[0]+1, cur_pos[1]])) is None:
                    new_positions.append([cur_pos[0]+1, cur_pos[1]])
                
                if piece_at(position_to_loc([cur_pos[0]-1, cur_pos[1]])) is None:
                    new_positions.append([cur_pos[0]-1, cur_pos[1]])

        # rook
        if piece in ('r1', 'r2', 'R1', 'R2'):

            cont = [True, True, True, True]
            for i in range(1, 8):
                if cont[0] == True:
                    if self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]+i])) is not None:
                        cont[0] = False
                    else:
                        new_positions.append([cur_pos[0], cur_pos[1]+i])
                
                if cont[1] == True:
                    if self.piece_at(position_to_loc([cur_pos[0], cur_pos[1]-i])) is not None:
                        cont[1] = False
                    else:
                        new_positions.append([cur_pos[0], cur_pos[1]-i])
                
                if cont[2] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]+i, cur_pos[1]])) is not None:
                        cont[2] = False
                    else:
                        new_positions.append([cur_pos[0]+i, cur_pos[1]])
                
                if cont[3] == True:
                    if self.piece_at(position_to_loc([cur_pos[0]-i, cur_pos[1]])):
                        cont[3] = False
                    else:
                        new_positions.append([cur_pos[0]-i, cur_pos[1]])

        # knight
        if piece in ('k1', 'K1', 'k2', 'K2'):

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
        new_locs = [position_to_loc(p) for p in new_positions]

        new_locs = [new_loc for new_loc in new_locs if
                    self.piece_at(new_loc) is None or self.is_white(new_loc) != self.is_white(loc)]
        return new_locs

    def move_piece(self, old_loc, new_loc):
        # creates a new board with the piece from the old loc to a new loc
        new_board = Board()
        new_board.positions = self.positions
        if new_loc in self.possible_moves(old_loc):
            new_board.set_piece_at(self.piece_at(old_loc), new_loc)
            new_board.set_piece_at(None, old_loc)
            return new_board
        else:
            return "Invalid."