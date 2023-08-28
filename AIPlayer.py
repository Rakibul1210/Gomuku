import random
class AIPlayer:
    def __init__(self, player_marker, depth=3):
        self.player_marker = player_marker
        self.max_depth = depth

    def make_move(self, game_state):
        # best_score = -float("inf")
        # best_move = None
        #
        # for move in available_moves(game_state):
        #     new_state = simulate_move(game_state, move)
        #     score = self.minimax(new_state, self.max_depth, False)
        #
        #     if score > best_score:
        #         best_score = score
        #         best_move = move
        #
        # return best_move

        r = random.randint(0,9)
        c = random.randint(0,9)
        return [r,c]

    # def minimax(self, game_state, depth, maximizing_player):
        # if depth == 0 or game_over(game_state):
        #     return evaluate(game_state, self.player_marker)
        #
        # if maximizing_player:
        #     best_score = -float("inf")
        #     for move in available_moves(game_state):
        #         new_state = simulate_move(game_state, move)
        #         score = self.minimax(new_state, depth - 1, False)
        #         best_score = max(best_score, score)
        #     return best_score
        # else:
        #     best_score = float("inf")
        #     for move in available_moves(game_state):
        #         new_state = simulate_move(game_state, move)
        #         score = self.minimax(new_state, depth - 1, True)
        #         best_score = min(best_score, score)
        #     return best_score
