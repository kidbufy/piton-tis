import random
import copy

# Function to make a move
def makemove(move, symbol):
    move = int(move) - 1
    global positions
    if positions[move] != "_":
        print("\nThis position is not empty.")
        return 0
    else:
        positions[move] = symbol
        return 1

# Function to check for a win
def checkwin():
    global positions
    global win_conditions
    # Define winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    # Check if any winning condition is met
    for condition in win_conditions:
        if all(positions[i] == "X" for i in condition):
            return "User"
        elif all(positions[i] == "O" for i in condition):
            return "AI"

    # Check for a tie
    if "_" not in positions:
        return "Tie"

    return 0

# Function for AI move
def aimove():
    global positions
    winner_move = checkwinai()
    resume = 1
    if winner_move != 0:
        makemove(winner_move, "O")
        return 1
    for condition in win_conditions:
        count_= 0
        countX = 0
        countO = 0
        for i in condition:
            if positions[i].count('_') == 1:
                count_ += 1
            elif positions[i].count('X') == 1:
                countX += 1
            elif positions[i].count('O') == 1:
                countO += 1
        if count_ == 2 and countO == 1:
            for i in condition:
                if positions[i] == "_":
                    makemove(i + 1, 'O')
                    resume = 0
                    return 1
                    break
            break
    if resume == 1:
        if positions[4] == "_":
            makemove(5, 'O')
            return 1
        elif positions[4] == "O" and all(position != "O" for position in positions[:4]) and all(position != "O" for position in positions[5:9]):
            move = random.choice(range(2, 10, 2))
            makemove(move, "O")
            return 1
        elif positions[4] == "X" and all(position != "X" for position in positions[:4]) and all(position != "X" for position in positions[5:9]):
            move = random.choice([1,3,7,9])
            makemove(move, "O")
            return 1
        else:
            while True:
                a = random.choice(range(1,10))
                if positions[a-1] == '_':
                    makemove(a,'O')
                    return 1

# Function to check AI's winning moves and user's blocking moves
def checkwinai():
    for i in range(1, 10):
        if positions[i - 1] == "_":
            positions[i - 1] = 'O'
            if checkwin() == "AI":
                positions[i - 1] = "_"
                return i
            positions[i - 1] = '_'
    for i in range(1, 10):
        if positions[i - 1] == "_":
            positions[i - 1] = 'X'
            if checkwin() == "User":
                positions[i - 1] = "_"
                return i
            positions[i - 1] = '_'
    return 0

# Function to end the game if a win or tie is reached
def endgame():
    if checkwin() != 0:
        map = "{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(positions[0], positions[1], positions[2], positions[3],
                                                      positions[4], positions[5], positions[6], positions[7], positions[8])
        print(map)
        if checkwin() == "AI":
            print("AI won lol. Maybe next time :)")
            exit()
        elif checkwin() == "User":
            print("Congratulations you won!")
            exit()
        elif checkwin() == "Tie":
            print("Tie! GG.")
            exit()
    else:
        pass

# Initial setup
print("TicTacToe!\n")
positions = ["_","_","_","_","_","_","_","_","_"]
positions2 = [x for x in range(1, 10)]
print("Positions: ", end='')
print(positions2)

# Game loop
while True:
    map = "{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(positions[0], positions[1], positions[2], positions[3],
                                                  positions[4], positions[5], positions[6], positions[7], positions[8])
    print('')
    print(map)

    user = input("Your move: ")
    if makemove(user, "X"):
        endgame()
        aimove()
        endgame()

    map = "{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n".format(positions[0], positions[1], positions[2], positions[3],
                                                  positions[4], positions[5], positions[6], positions[7], positions[8])
