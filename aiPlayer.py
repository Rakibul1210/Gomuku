from minimax2 import Minimax
class AIPlayer:
    def __init__(self, player_marker):
        self.player_marker = player_marker
        self.minimax = Minimax()

    def make_move(self, board):
        print(f"{self.player_marker}'s turn (AI)")

        # Define the depth for minimax search (you can adjust this)
        depth = 2

        # Calculate the next move using the Minimax algorithm
        move = self.minimax.calculateNextMove(depth, board, self.player_marker)

        if move is not None and all(isinstance(coord, int) for coord in move):
            row, col = move[0], move[1]
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '_':
                print(f"AI's move: Row {row + 1}, Column {col + 1}")
                return row, col

        print("AI couldn't find a valid move.")
        return None, None


# from minimax import Minimax
# class AIPlayer:
#     def __init__(self, player_marker, max_depth=3):
#         self.player_marker = player_marker
#         self.max_depth = max_depth
#
#     def make_move(self, game_state):
#         # Generate all possible moves
#         possible_moves = self.generate_possible_moves(game_state)
#
#         # Initialize variables to keep track of the best move and score
#         best_move = None
#         best_score = -float("inf")
#         alpha = -float("inf")
#         beta = float("inf")
#
#         # Evaluate and find the best move using minimax with alpha-beta pruning
#         for move in possible_moves:
#             new_state = self.simulate_move(game_state, move)
#             score = Minimax.minimaxSearchAB(new_state, self.max_depth, alpha, beta)
#
#             if score > best_score:
#                 best_score = score
#                 best_move = move
#
#             alpha = max(alpha, best_score)
#
#         return best_move
#
#     def generate_possible_moves(self, game_state):
#         possible_moves = []
#         for row in range(len(game_state)):
#             for col in range(len(game_state[0])):
#                 if game_state[row][col] == "_":
#                     possible_moves.append((row, col))
#         return possible_moves
#
#     def simulate_move(self, game_state, move):
#         row, col = move
#         new_state = [list(row_data) for row_data in game_state]
#         new_state[row][col] = self.player_marker
#         return new_state
#
#     def minimax(self, game_state, depth, alpha, beta, maximizing_player):
#         if depth == 0 or self.is_game_over(game_state):
#             controller = Controller()
#             return controller.evaluate(game_state)
#
#         if maximizing_player:
#             best_score = -float("inf")
#             for move in self.generate_possible_moves(game_state):
#                 new_state = self.simulate_move(game_state, move)
#                 score = self.minimax(new_state, depth - 1, alpha, beta, False)
#                 best_score = max(best_score, score)
#                 alpha = max(alpha, best_score)
#
#                 if beta <= alpha:
#                     break  # Beta cutoff, prune the rest of the branches
#             return best_score
#         else:
#             best_score = float("inf")
#             for move in self.generate_possible_moves(game_state):
#                 new_state = self.simulate_move(game_state, move)
#                 score = self.minimax(new_state, depth - 1, alpha, beta, True)
#                 best_score = min(best_score, score)
#                 beta = min(beta, best_score)
#
#                 if beta <= alpha:
#                     break  # Alpha cutoff, prune the rest of the branches
#             return best_score

#
#
