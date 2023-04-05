# queen = 9
# king = 0
# bishop = 3
# knight = 3
# rook = 5
# pawn = 1

# bishop_move = []

# pieces = {'Q': [4, 1], 'K': [5, 1], 'B1': [3, 1], 'B2': [6, 1], 'N1': [2, 1], 'N2': [7, 1], 'R1': [1, 1],
#           'R2': [8, 1], 'P1': [1, 2], 'P2': [2, 2], 'P3': [3, 2], 'P4': [4, 2], 'P5': [5, 2], 'P6': [6, 2], 'P7': [7, 2], 'P8': [8, 2], 'q': [4, 8], 'k': [5, 8], 'bb': [3, 8], 'b': [6, 8], 'nn': [2, 8], 'n': [7, 8], 'rr': [1, 8],
#           'r': [8, 8], 'pa': [1, 7], 'pb': [2, 7], 'pc': [3, 7], 'pd': [4, 7], 'pe': [5, 7], 'pf': [6, 7], 'pg': [7, 7], 'ph': [8, 7]}


# pcs_nxt_2_king_white = 0
# pcs_nxt_2_king_black = 0
# safety = 0
# space = 0
# material = 0
# # calculate material
# for piece in pieces:
#     if piece == 'Q':
#         material += queen

#     elif piece == 'B1' or piece == 'B2':
#         material += bishop
#     elif piece == 'N1' or piece == 'N2':
#         material += knight
#     elif piece == 'R1' or piece == 'R2':
#         material += rook
#     elif piece == 'P1' or piece == 'P2' or piece == 'P3' or piece == 'P4' or piece == 'P5' or piece == 'P6' or piece == 'P7' or piece == 'P8':
#         material += pawn
#     elif piece == 'q':
#         material -= queen
#     elif piece == 'bb' or piece == 'b':
#         material -= bishop
#     elif piece == 'nn' or piece == 'n':
#         material -= knight
#     elif piece == 'rr' or piece == 'r':
#         material -= rook
#     elif piece == 'pa' or piece == 'pb' or piece == 'pc' or piece == 'pd' or piece == 'pe' or piece == 'pf' or piece == 'pg' or piece == 'ph':
#         material -= pawn

# # calculate king safety

# # calculate space


# loc = input("What square would you like to check? ")


# def loc_to_position(loc):
#     x = ord(loc[0]) - ord('a')+1
#     y = int(loc[1])
#     return [x, y]
# # board


# class Board:
#     def __init__(self, positions):
#         self.positions = positions

#     def move(self, piece, new_space):
#         new_positions = self.positions.copy()
#         new_positions[piece] = new_space
#         return Board(new_positions)

#     def score(self, material, king_safety, space):
#         score = 0
#         score += material
#         score += space * 0.75
#         score += king_safety

#         return score

#     def at(self, loc):
#         position = loc_to_position(loc)
#         piece = None
#         for type, pos in self.positions.items():
#             if pos == position:
#                 piece = type
#         return piece


# def main():
#     board = Board(pieces)

#     next_spaces = board.move("b1", [2, 1])

#     print("Currently on [2,1]")

#     for position in next_spaces:
#         print(position)

#     get_eval = board.score(material, safety, space)
#     get_piece = board.at(loc)
#     print(f"The piece on that square is {get_piece}")
#     print(f"The evaluation is {get_eval}")


# main()

# real
# real
# real
# real
# real
# real
# real


def loc_to_position(loc):
    return ord(loc[0])-ord('a'), int(loc[1])-1


def get_color(loc, board):
    color = None
    if (n := board.piece_at(loc)) in [p for p in pieces if p[0].islower()]:
        color = False
    elif n in [p for p in pieces if p[0].isupper()]:
        color = True

    return color


pieces = ['p1', 'P1', 'p2', 'P2', 'p3', 'P3', 'p4', 'P4', 'p5', 'P5', 'p6', 'P6', 'p7', 'P7', 'p8',
          'P8', 'q', 'Q', 'k', 'K', 'b1', 'B1', 'b2', 'B2', 'k1', 'K1', 'k2', 'K2', 'r1', 'R1', 'r2', 'R2']


class Board(object):
    def __init__(self):
        self.positions = [[None for i in range(8)] for j in range(8)]

    def piece_at(self, loc):
        pos = loc_to_position(loc)
        return self.positions[pos[0]][pos[1]]

    def move(self, piece, cur_pos):

        new_positions = []

# bishop
        if piece in ('b1', 'b2', 'B1', 'B2'):

            for i in range(1, 8):
                new_positions.append([cur_pos[0]-i, cur_pos[1]-i])
                new_positions.append([cur_pos[0]-i, cur_pos[1]+i])
                new_positions.append([cur_pos[0]+i, cur_pos[1]-i])
                new_positions.append([cur_pos[0]+i, cur_pos[1]+i])

# pawn
        if piece in ("p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "P1", 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'):
            new_positions.append([cur_pos[0], cur_pos[1]+1])
            if cur_pos[1] == 2 or cur_pos[1] == 7:
                new_positions.append([cur_pos[0], cur_pos[1]+2])
            if (n := get_color([cur_pos[0]+1, cur_pos[1]+1], self)):
                if (y := get_color(cur_pos, self)):
                    pass
                else:
                    new_positions.append([cur_pos[0]+1, cur_pos[1]+1])
            elif n == False:
                if y:
                    new_positions.append([cur_pos[0]+1, cur_pos[1]+1])
                else:
                    pass
            else:
                pass

            if (n := get_color([cur_pos[0]-1, cur_pos[1]+1], self)):
                if (y := get_color(cur_pos, self)):
                    pass
                else:
                    new_positions.append([cur_pos[0]-1, cur_pos[1]+1])
            elif n == False:
                if y:
                    new_positions.append([cur_pos[0]-1, cur_pos[1]+1])
                else:
                    pass
            else:
                pass

# queen
        if piece in ('q', 'Q'):

            for i in range(1, 8):
                new_positions.append([cur_pos[0]-i, cur_pos[1]-i])
                new_positions.append([cur_pos[0]-i, cur_pos[1]+i])
                new_positions.append([cur_pos[0]+i, cur_pos[1]-i])
                new_positions.append([cur_pos[0]+i, cur_pos[1]+i])
                new_positions.append([cur_pos[0], cur_pos[1]+i])
                new_positions.append([cur_pos[0], cur_pos[1]-i])
                new_positions.append([cur_pos[0]+i, cur_pos[1]])
                new_positions.append([cur_pos[0]-i, cur_pos[1]])

# king
        if piece in ('k', 'K'):

            for i in range(1, 8):
                new_positions.append([cur_pos[0]-1, cur_pos[1]-1])
                new_positions.append([cur_pos[0]-1, cur_pos[1]+1])
                new_positions.append([cur_pos[0]+1, cur_pos[1]-1])
                new_positions.append([cur_pos[0]+1, cur_pos[1]+1])
                new_positions.append([cur_pos[0], cur_pos[1]+1])
                new_positions.append([cur_pos[0], cur_pos[1]-1])
                new_positions.append([cur_pos[0]+1, cur_pos[1]])
                new_positions.append([cur_pos[0]-1, cur_pos[1]])

# rook
        if piece in ('q', 'Q'):

            for i in range(1, 8):
                new_positions.append([cur_pos[0], cur_pos[1]+i])
                new_positions.append([cur_pos[0], cur_pos[1]-i])
                new_positions.append([cur_pos[0]+i, cur_pos[1]])
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

        new_positions = [p for p in new_positions if p[0]
                         > 0 and p[1] > 0 and p[0] < 9 and p[1] < 9]

        return new_positions


board = Board()
new_locations = board.move('p1', 'a2')
print(new_locations)
