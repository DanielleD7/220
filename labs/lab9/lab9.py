"""
Name: Danielle Di Pace
lab9.py

Problem: A repeatable game of tic-tac-toe

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


# Creates the numbers associated with the tic-tac-toe board
def build_board():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


# Checks if the player's chosen position is legal
def is_legal(board, position):
    if str(board[position - 1]).isnumeric():
        return True
    return False


# Fill in the chosen position with the player's shape
def fill_spot(board, position, shape):
    shape = shape.strip().lower()
    board[position - 1] = shape


# Checks if the game has been won
def game_is_won(board):
    # Horizontal Check
    for spot in range(0, 9, 3):
        if board[spot] == board[spot + 1] == board[spot + 2]:
            return True
    # END Horizontal Check Loop

    # Vertical Check
    for spot in range(0, 3):
        if board[spot] == board[spot + 3] == board[spot + 6]:
            return True
    # END Vertical Check Loop

    # Top L->R Diagonal Check
    spot = 0
    if board[spot] == board[spot + 4] == board[spot + 8]:
        return True

    # Top R->L Diagonal Check
    if board[spot + 2] == board[spot + 4] == board[spot + 6]:
        return True

    # No win
    return False


# Checks if the current game is over
def game_over(board):
    if game_is_won(board):
        return True

    # Searching for space on the board
    for value in board:
        if str(value).isnumeric():
            return False
    return True


# Returns the winner of the game
def get_winner(board):
    x_count = 0
    y_count = 0

    for value in board:
        if value == "x":
            x_count = x_count + 1
        if value == "o":
            y_count = y_count + 1

    if x_count > y_count:
        return "x"
    if x_count == y_count:
        return "o"
    else:
        return None


# Plays a game of tic-tac-toe
def play(board):
    # Instructions
    print("Welcome to Tic-Tac-Toe!")
    print("To Play, each player will take turns entering a number.")
    print("The numbers on the board corresponds to the position you would like to mark.")
    print("Player 1 will be x and player 2 will be o.")

    new_game = True
    count = 0
    print_board(board)

    while new_game:
        while not game_over(board):
            if count % 2:
                shape = "o"
            else:
                shape = "x"

            print(shape + "'s, choose a position:")
            position = eval(input(""))

            # While position is not legal
            while not is_legal(board, position):
                print("Position", position, "is not legal.")
                print(shape + "'s, choose a new position:")
                position = eval(input(""))

            fill_spot(board, position, shape)
            print_board(board)
            count = count + 1
        # END game not over loop

        if game_is_won(board):
            print(get_winner(board) + " wins!")
        else:
            print("Tie!")

        # Asking for new game
        response = input("\nWould you like to play a new game? (Yes or No) ")
        if response[0].upper() == "Y":
            new_game = True
            count = 0
            board = build_board()
            print_board(board)
        else:
            new_game = False
    # END New Game While Loop

    print("\nThank you for playing!")


def main():
    play(build_board())


if __name__ == '__main__':
    main()
