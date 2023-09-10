from gomokuGame import GomokuGame
from aiPlayer import AIPlayer
import time


if __name__ == "__main__":
    print("Welcome to Gomoku!")
    game_mode = int(input("Choose game mode:\n1. Player vs. Player\n2. Player vs. AI\n"))

    if game_mode == 2:
        ai_player = AIPlayer(player_marker='B')

    game = GomokuGame()
    game.display_board()

    while True:
        print(f"\t{game.current_player}'s turn")

        try:
            row = int(input(f"Enter row (1-{game.board_size}): ")) - 1
            col = int(input(f"Enter column (1-{game.board_size}): ")) - 1
        except:
            print("Invalid input type!!")
            continue

        if game.make_move(row, col):
            game.display_board()
            if game.check_win_condition():
                print("\n\t" + ("B WON" if game.current_player == "W" else "A WON"))
                break
        else:
            print("Invalid move. Try again.")

        if game_mode == 2 and game.current_player == 'B':

            start_time = time.time()
            ai_move = ai_player.make_move(game.board)
            end_time = time.time();

            print("Time taken: ", end_time - start_time)
            print(f"AI's move: {ai_move}")
            game.make_move(ai_move[0], ai_move[1])
            game.display_board()
            if game.check_win_condition():
                print("\n\t" + ("B WON" if game.current_player == "W" else "AI WON"))
                break
