class GomokuGame:
    def __init__(self, board_size=10):
        self.board_size = board_size
        self.board = [['_' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'B'  # 'X' represents Player 1, 'O' represents Player 2

    def switch_player(self):
        if self.current_player == 'B':
            self.current_player = 'W'
        else:
            self.current_player = 'B'

    def make_move(self, row, col):
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '_':
            self.board[row][col] = self.current_player
            self.switch_player()
            return True
        return False

    def display_board(self):
        for row in self.board:
            print(' '.join(row))


# Test the implementation
if __name__ == "__main__":
    game = GomokuGame()
    game.display_board()

    while True:
        print(f"\t{game.current_player}'s turn")
        row = int(input(f"Enter row (1-{game.board_size}): ")) - 1
        col = int(input(f"Enter column (1-{game.board_size}): ")) - 1

        print(row, col)

        if game.make_move(row, col):
            game.display_board()
        else:
            print("Invalid move. Try again.")
