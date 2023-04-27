from chess import *

class LookAheadPlayer(object):

    def __init__(self, analyzer_class, depth=1):
        self.analyzer_class = analyzer_class
        self.depth = depth
        self.visited_boards = {}

    def get_possible_next_move(self, board, color):
        """
        Given a board and a color, returns list of possible next moves by that
        color. Each move is a (old_location, new_location) tuple.
        """

        moves = []
        my_pieces = [piece for piece in board.pieces()
                     if piece_color(piece) == color]

        for piece in my_pieces:
            old_location = board.location_of(piece)
            for new_location in board.possible_moves(old_location):
                moves.append((old_location, new_location))

        return moves

    def get_next_moves(self, board, color):
        """
	Given a board and a color, return list of Move objects.
        """

        promote_to = get_piece('q', color)
        move_and_new_boards = []

        for old_location, new_location in self.get_possible_next_move(board, color):
            try:
                new_board = board.move_piece(
                    old_location, new_location, promotion=promote_to)
            except InvalidMoveException as e:
                pass
            else:
                move_and_new_boards.append(
                    Move((old_location, new_location),
                         new_board,
                         color)
                )

        return move_and_new_boards

    def get_future_moves(self, board, color, depth):
        """
	Given a starting board and a color, return a list of sequences of Move
	objects, where the number of Move objects in a sequence is no more than
        the depth argument (it may be less because of check-mates).
        """

        assert depth > 0
        next_moves = self.get_next_moves(board, color)

        if depth == 1:
            for m in next_moves:
                self.visited_boards[m.new_board.key()] = 1
            return [[m] for m in next_moves]

        else:
            all_moves = []

            for last_move in next_moves:
                # there is a checkmate stop searching
                if last_move.new_board.check_mate(last_move.next_move_color):
                    self.visited_boards[last_move.new_board.key()] = 1
                    all_moves.append([last_move])

                # don't evaluate a board we've already evaluated
                elif last_move.new_board.key() in self.visited_boards:
                    all_moves.append([last_move])

                else:
                    self.visited_boards[last_move.new_board.key()] = 1
                    future_moves = self.get_future_moves(
                        last_move.new_board, last_move.next_move_color, depth-1)
                    for move_sequence in future_moves:
                        move_sequence = [last_move] + move_sequence
                        all_moves.append(move_sequence)

            return all_moves

    def computer_turn(self, board, color):
        best_move = None
        best_score = None
        cur_score = 0

        self.visited_boards = {}
        worst_future_moves = []
        all_moves = self.get_future_moves(board, color, self.depth)
        already_lined = []

        for line in all_moves:
            first_move = line[0].move
            if first_move[0] not in already_lined:
                already_lined.append([first_move])
            else:
                for list in already_lined:
                    if list[0][0][0] == first_move[0]:
                        list.append(first_move)
        
        for line in already_lined:
            worst_score = None
            worst_move = None
            worst_old_loc = None
            for move in line:
                old_loc = move[0]
                new_board = board.duplicate()
                new_board = new_board.move_piece(move[0], move[1])
                analyzer = self.analyzer_class(new_board)
                cur_score - analyzer.score(color, new_board)
                if (color == Board.WHITE and (worst_score is None or cur_score < worst_score)) or \
                        (color == Board.BLACK and (worst_score is None or cur_score > worst_score)):
                    worst_score = cur_score
                    worst_old_loc = old_loc
                    worst_move = move[1]
            
            worst_future_moves.append([worst_old_loc, worst_move])


        for line in all_moves:
            first_move = line[0].move
            first_move_resulting_board = line[0].new_board
            second_move_color = line[0].next_move_color
            ending_board = line[-1].new_board

            if first_move_resulting_board.check_mate(second_move_color):
                return first_move
            elif first_move_resulting_board.check_mate(color):
                continue

        for line in worst_future_moves:
            first_move = line[0].move
            first_move_resulting_board = line[0].new_board
            second_move_color = line[0].next_move_color
            ending_board = line[-1].new_board

            if first_move_resulting_board.check_mate(second_move_color):
                return first_move
            elif first_move_resulting_board.check_mate(color):
                continue

            analyzer = self.analyzer_class(ending_board)
            cur_score = analyzer.score(color, board)
            # print("scoring", first_move[0], "to", first_move[1], "score is", cur_score)
            if (color == Board.WHITE and (best_score is None or cur_score > best_score)) or \
                    (color == Board.BLACK and (best_score is None or cur_score < best_score)):
                best_score = cur_score
                best_move = first_move

        if best_move is None:  # cannot make a move
            if board.check_mate(color):
                raise GameOverException(f"Checkmate, {color} lost.")
            else:
                raise GameOverException("Draw by stalemate.")

        return best_move
