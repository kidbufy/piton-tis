#Added multiplayer mode and scoreboard


import random
import copy
import time


# Function to make a move
def make_move(position_index, symbol):
    position_index = int(position_index) - 1
    global board_positions
    if board_positions[position_index] != "_":
        print("\nThis position is not empty.")
        return 0
    else:
        board_positions[position_index] = symbol
        return 1


# Function to check for a win
def check_win():
    global board_positions
    global win_conditions
    # Define winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    # Check if any winning condition is met
    for condition in win_conditions:
        if all(board_positions[i] == "X" for i in condition):
            return "player1"
        elif all(board_positions[i] == "O" for i in condition):
            return "player2"

    # Check for a tie
    if "_" not in board_positions:
        return "Tie"

    return 0


# Function for AI move
def ai_move_decider():
    global board_positions
    global win_conditions

    available_moves = range(1, 10)
    center_position = 4
    user_centered = (
        all(position == "_" for position in board_positions[:center_position])
        and all(position == "_" for position in board_positions[:center_position])
    )

    if board_positions[center_position] == "_":
        make_move(5, "O")
    elif board_positions[center_position] == "X" and user_centered:
        corners = [x for x in range(1, 10, 2) if x != 5]
        make_move(random.choice(corners), "O")
    else:
        winner_move = check_winner_move()
        if winner_move != 0:
            make_move(winner_move, "O")
        else:
            while True:
                move = random.choice(range(1, 10))
                if board_positions[move - 1] == "_":
                    make_move(move, "O")
                    break


# Function to check AI's winning moves and user's blocking moves
def check_winner_move():
    global board_positions

    available_moves = range(1, 10)
    for position_to_check in available_moves:
        if board_positions[position_to_check - 1] == "_":
            board_positions[position_to_check - 1] = "O"
            if check_win() == "player2":
                board_positions[position_to_check - 1] = "_"
                return position_to_check
            board_positions[position_to_check - 1] = "_"
    for position_to_check in available_moves:
        if board_positions[position_to_check - 1] == "_":
            board_positions[position_to_check - 1] = "X"
            if check_win() == "player1":
                board_positions[position_to_check - 1] = "_"
                return position_to_check
            board_positions[position_to_check - 1] = "_"
    return 0


# Function to end the game if a win or tie is reached
def check_end_game():
    global board_positions
    global game_map
    global player_score
    global player2_score

    update_game_map()
    print(game_map)
    winning_player = check_win()
    if winning_player:
        if winning_player == "player2":
            print("Congratulations! " + player2_name + " won!")
            player2_score = player2_score + 1
        elif winning_player == "player1":
            print("Congratulations! " + player1_name + " won!")
            player_score = player_score + 1
        elif winning_player == "Tie":
            print("It's a tie! GG.")
        print(player1_name + ": " + str(player_score) + "\n" + player2_name + ": " + str(player2_score) + "\n")
        available_moves = False
        while True:
            resume = input("Do you want to play again (Y/N): ").upper()
            if resume == "Y":
                return 1
            elif resume == "N":
                print("Goodbye!")
                exit()
            else:
                print("You should enter Y or N")
    else:
        return 0


def update_game_map():
    global game_map
    global board_positions
    game_map = "{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(
        board_positions[0], board_positions[1], board_positions[2],
        board_positions[3], board_positions[4], board_positions[5],
        board_positions[6], board_positions[7], board_positions[8]
    )


# Initial setup
player_score = 0
player2_score = 0
player1_name = None
player2_name = None

print("TicTacToe!\n")
while True:
    game_mode = input("Do you want to play in single or multi player mode? (S/M): ").upper()
    if game_mode == "M":
        player1_name = input("First player's name: ")
        player2_name = input("Second player's name: ")
        break
    elif game_mode == "S":
        player1_name = input("Enter your name: ")
        player2_name = "AI"
        break
    else:
        print("You should enter S or M.")

while True:
    board_positions = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    print("Positions: \n1,2,3\n4,5,6\n7,8,9\n")

    game_map = "{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(
        board_positions[0], board_positions[1], board_positions[2],
        board_positions[3], board_positions[4], board_positions[5],
        board_positions[6], board_positions[7], board_positions[8]
    )
    print(game_map)
    # Game loop
    available_moves = False
    while not available_moves:
        try:
            player1_move = input(player1_name + "'s move: ")
            if make_move(player1_move, "X"):
                available_moves = check_end_game()

                if not available_moves and game_mode == "S":
                    time.sleep(0.8)
                    ai_move_decider()
                    available_moves = check_end_game()

                if not available_moves and game_mode == "M":
                    while True:
                        try:
                            player2_move = input(player2_name + "'s move:")
                            if make_move(player2_move, "O"):
                                available_moves = check_end_game()
                                break
                        except ValueError:
                            print("You should enter a valid number.")
                        except IndexError:
                            print("You should enter a valid number in [1,9]")

        except ValueError:
            print("You should enter a valid number.")
        except IndexError:
            print("You should enter a valid number in [1,9]")
