from gomokuGame import GomokuGame
from aiPlayer import AIPlayer
import time
import pygame

pygame.init()

ai_player = AIPlayer(player_marker='B')
window_width = 500
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gomoku")

background_color = (70, 39, 25)  # RGB values for darker wood color
board_color = (159, 100, 60)  # RGB values for light wood color
black = (0, 0, 0)
white = (255, 255, 255)

board_size = 10
board_cell_size = 35
board_offset = ((window_width - board_size * board_cell_size) // 2, (window_height - board_size * board_cell_size) // 2)

checker_radius = board_cell_size // 2

# Initialize game state
game_board = [['' for _ in range(board_size)] for _ in range(board_size)]
current_player = 0  # 'X' starts the game

if __name__ == "__main__":
    pygame.init()
    # print("Welcome to Gomoku!")
    # game_mode = int(input("Choose game mode:\n1. Player vs. Player\n2. Player vs. AI\n"))

    # if game_mode == 2:

    game = GomokuGame()
    # game.display_board()
    # print("HIIIIIIIIIIi")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and current_player == 0:
                x, y = event.pos
                row = (y - board_offset[1]) // board_cell_size
                col = (x - board_offset[0]) // board_cell_size
                print(current_player)
                if 0 <= row < board_size and 0 <= col < board_size and game_board[row][col] == '':
                    game_board[row][col] = current_player
                    if game.make_move(row, col):
                        if game.check_win_condition():
                            print("\n\t" + ("AI WON" if game.current_player == "W" else "Player WON"))
                            break
                    else:
                        print("Invalid move. Try again.")
                else:
                    continue
                current_player = not current_player
                continue

            elif current_player == 1:
                ai_move = ai_player.make_move(game.board)
                game_board[ai_move[0]][ai_move[1]] = current_player
                game.make_move(ai_move[0], ai_move[1])

                if game.check_win_condition():
                    print("\n\t" + ("AI WON" if game.current_player == "W" else "PLayer WON"))
                    break
                current_player = not current_player

        # Clear the screen
        screen.fill(background_color)

        # Draw the smaller game board
        pygame.draw.rect(screen, board_color,
                         (board_offset[0], board_offset[1], board_size * board_cell_size, board_size * board_cell_size))
        for row in range(board_size):
            for col in range(board_size):
                pygame.draw.rect(screen, white, (
                board_offset[0] + col * board_cell_size, board_offset[1] + row * board_cell_size, board_cell_size,
                board_cell_size), 1)

        # Draw the checkers
        for row in range(board_size):
            for col in range(board_size):
                if game_board[row][col] == 0:
                    pygame.draw.circle(screen, black, (
                    board_offset[0] + col * board_cell_size, board_offset[1] + row * board_cell_size), checker_radius)
                elif game_board[row][col] == 1:
                    pygame.draw.circle(screen, white, (
                    board_offset[0] + col * board_cell_size, board_offset[1] + row * board_cell_size), checker_radius)

        # Update the display
        pygame.display.flip()

    pygame.quit()
# from gomokuGame import GomokuGame
# from aiPlayer import AIPlayer
# import time
#
#
# if __name__ == "__main__":
#     print("Welcome to Gomoku!")
#     game_mode = int(input("Choose game mode:\n1. Player vs. Player\n2. Player vs. AI\n"))
#
#     if game_mode == 2:
#         ai_player = AIPlayer(player_marker='B')
#
#     game = GomokuGame()
#     game.display_board()
#
#     while True:
#         print(f"\t{game.current_player}'s turn")
#
#         try:
#             row = int(input(f"Enter row (1-{game.board_size}): ")) - 1
#             col = int(input(f"Enter column (1-{game.board_size}): ")) - 1
#         except:
#             print("Invalid input type!!")
#             continue
#
#         if game.make_move(row, col):
#             game.display_board()
#             if game.check_win_condition():
#                 print("\n\t" + ("B WON" if game.current_player == "W" else "A WON"))
#                 break
#         else:
#             print("Invalid move. Try again.")
#
#         if game_mode == 2 and game.current_player == 'B':
#
#             start_time = time.time()
#             ai_move = ai_player.make_move(game.board)
#             end_time = time.time();
#
#             print("Time taken: ", end_time - start_time)
#             print(f"AI's move: {ai_move}")
#             game.make_move(ai_move[0], ai_move[1])
#             game.display_board()
#             if game.check_win_condition():
#                 print("\n\t" + ("B WON" if game.current_player == "W" else "AI WON"))
#                 break
