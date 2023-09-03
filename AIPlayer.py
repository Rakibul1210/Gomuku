
class AIPlayer:
    def __init__(self, player_marker, max_depth=3):
        self.player_marker = player_marker
        self.max_depth = max_depth

    def make_move(self, game_state):
        # Generate all possible moves
        possible_moves = self.generate_possible_moves(game_state)

        # Initialize variables to keep track of the best move and score
        best_move = None
        best_score = -float("inf")
        alpha = -float("inf")
        beta = float("inf")

        # Evaluate and find the best move using minimax with alpha-beta pruning
        for move in possible_moves:
            new_state = self.simulate_move(game_state, move)
            score = self.minimax(new_state, self.max_depth, alpha, beta, False)

            if score > best_score:
                best_score = score
                best_move = move

            alpha = max(alpha, best_score)

        return best_move

    def generate_possible_moves(self, game_state):
        possible_moves = []
        for row in range(len(game_state)):
            for col in range(len(game_state[0])):
                if game_state[row][col] == "_":
                    possible_moves.append((row, col))
        return possible_moves

    def simulate_move(self, game_state, move):
        row, col = move
        new_state = [list(row_data) for row_data in game_state]
        new_state[row][col] = self.player_marker
        return new_state

    def minimax(self, game_state, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_game_over(game_state):
            return self.evaluate(game_state)

        if maximizing_player:
            best_score = -float("inf")
            for move in self.generate_possible_moves(game_state):
                new_state = self.simulate_move(game_state, move)
                score = self.minimax(new_state, depth - 1, alpha, beta, False)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break  # Beta cutoff, prune the rest of the branches
            return best_score
        else:
            best_score = float("inf")
            for move in self.generate_possible_moves(game_state):
                new_state = self.simulate_move(game_state, move)
                score = self.minimax(new_state, depth - 1, alpha, beta, True)
                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if beta <= alpha:
                    break  # Alpha cutoff, prune the rest of the branches
            return best_score

    def evaluate(self, game_state):
        # Implement your evaluation function here
        # This function should return a score indicating the desirability of the game state
        pass
