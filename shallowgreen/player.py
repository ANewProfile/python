from chess import *

class LookAheadPlayer(object):

    def __init__(self, analyzer_class, depth=1):
        if depth > 1 and depth%2 != 0:
            raise Exception("Beyond depth 2, depth must be even integer")

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
        self.visited_boards = {}
        all_moves = self.get_future_moves(board, color, self.depth)
        first_move_scores = {}
        assert self.depth == 1 or self.depth%2 == 0

        for move_sequence in all_moves:
            first_move = move_sequence[0].move
            first_move_resulting_board = move_sequence[0].new_board
            second_move_color = move_sequence[0].next_move_color
            ending_board = move_sequence[-1].new_board
            ending_move = move_sequence[-1].move

            if first_move_resulting_board.check_mate(second_move_color):
                return first_move

            analyzer = self.analyzer_class(ending_board)
            cur_score = analyzer.score(move_sequence[-1].just_moved_color)

            if DEBUG_MOVE:
                print("first move %s%s, end board score after %s move %s%s = %.4f, tracking for %s" % (
                  first_move[0], first_move[1],
                  move_sequence[-1].just_moved_color, ending_move[0], ending_move[1],
                  cur_score, color))

            if first_move not in first_move_scores:
                first_move_scores[first_move] = cur_score
            elif analyzer.worse_score(color, first_move_scores[first_move], cur_score) == cur_score:
                first_move_scores[first_move] = cur_score

        best_move = None
        best_score = None
        for first_move, first_move_score in first_move_scores.items():
            if DEBUG_MOVE:
                print("first move %s%s, score %.4f, color %s" % (first_move[0], first_move[1], first_move_score, color))
            if best_score is None or analyzer.better_score(color, best_score, first_move_score) == first_move_score:
                best_score = first_move_score
                best_move = first_move

        if best_move is None:  # cannot make a move
            if board.check_mate(color):
                raise GameOverException(f"Checkmate, {color} lost.")
            else:
                raise GameOverException("Draw by stalemate.")

        return best_move
