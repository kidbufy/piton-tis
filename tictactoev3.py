import random
import time

# Define winning combinations
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

# Function to make a move
def make_move(player, board_positions):
    print_game_map(board_positions)
    if player.name == "AI":
        time.sleep(0.6)
        move = int(ai_move_decider(board_positions)) - 1
    else:
        while True:
            try:
                move = int(input(player.name + "'s move: ")) - 1
                if board_positions[move] != "_":
                    print("This position is not empty!")
                else:
                    break
            except ValueError:
                print("You should enter a number.")
            except IndexError:
                print("You should enter a valid number")

    board_positions[move] = player.symbol
    return check_end_game(player1, player2, board_positions)

# Function to check for a win
def check_win(board_positions):
    for condition in win_conditions:
        if all(board_positions[i] == "X" for i in condition):
            return player1
        elif all(board_positions[i] == "O" for i in condition):
            return player2

    if "_" not in board_positions:
        return "Tie"

    return 0

# Function for AI move
def ai_move_decider(board_positions):
    center_position = 4
    user_centered = all(position == "_" for position in board_positions[:9] if position != 4)

    if board_positions[center_position] == "_":
        return 5
    elif board_positions[center_position] == "X" and user_centered:
        corners = [x for x in range(1, 10, 2) if x != 5]
        return random.choice(corners)
    else:
        winner_move = check_winner_move(board_positions)
        if winner_move != 0:
            return winner_move
        else:
            while True:
                move = random.choice(range(1, 10))
                if board_positions[move - 1] == "_":
                    return move

# Function to check AI's winning moves and user's blocking moves
def check_winner_move(board_positions):
    available_moves = range(1, 10)
    for position_to_check in available_moves:
        if board_positions[position_to_check - 1] == "_":
            board_positions[position_to_check - 1] = "O"
            if check_win(board_positions) == player2:
                board_positions[position_to_check - 1] = "_"
                return position_to_check
            board_positions[position_to_check - 1] = "_"
    for position_to_check in available_moves:
        if board_positions[position_to_check - 1] == "_":
            board_positions[position_to_check - 1] = "X"
            if check_win(board_positions) == player1:
                board_positions[position_to_check - 1] = "_"
                return position_to_check
            board_positions[position_to_check - 1] = "_"
    return 0

# Function to end the game if a win or tie is reached
def check_end_game(player1, player2, board_positions):
    winning_player = check_win(board_positions)
    if winning_player != 0:
        print_game_map(board_positions)
        if winning_player != "Tie":
            print("Congratulations! " + winning_player.name + " won!")
            winning_player.score += 1
        else:
            print("It's a tie! GG.")
        print(player1.name + ": " + str(player1.score) + "\n" + player2.name + ": " + str(player2.score) + "\n")
        while True:
            resume = input("Do you want to play again (Y/N): ").upper()
            if resume == "Y":
                return True
            elif resume == "N":
                print("Goodbye!")
                exit()
            else:
                print("You should enter Y or N")
    else:
        return False

def print_game_map(board_positions):
    game_map = "{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(
        board_positions[0], board_positions[1], board_positions[2],
        board_positions[3], board_positions[4], board_positions[5],
        board_positions[6], board_positions[7], board_positions[8]
    )
    print(game_map)

# Initial setup
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

def setup_game():
    return ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

def create_game_map(board):
    return "{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(
        board[0], board[1], board[2],
        board[3], board[4], board[5],
        board[6], board[7], board[8]
    )

def ask_for_game_mode():
    while True:
        game_mode = input("Do you want to play in single or multi-player mode? (S/M): ").upper()
        if game_mode == "M":
            player1 = Player(input("First player's name: "), "X")
            player2 = Player(input("Second player's name: "), "O")
            return player1, player2
        elif game_mode == "S":
            player1 = Player(input("First player's name: "), "X")
            player2 = Player("AI", "O")
            return player1, player2
        else:
            print("You should enter S or M.")

print("TicTacToe!\n")
player1, player2 = ask_for_game_mode()
while True:
    board_positions = setup_game()
    # Game loop
    game_over = False
    while not game_over:
        game_over = make_move(player1, board_positions)
        if not game_over:
            game_over = make_move(player2, board_positions)
