"""
Name: Danielle Di Pace
hw9.py

Problem: A game of hangman in the command line and a version using graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import GraphWin, Point, Line, Circle, Text, Entry


def get_words(file_name):
    word_file = open(file_name, "r")
    word_list = word_file.readlines()
    word_file.close()
    return word_list


def get_random_word(words):
    index = randint(0, len(words) - 1)
    random_word = words[index].replace("\n", "")
    return random_word


def letter_in_secret_word(letter, secret_word):
    for secret_letter in secret_word:
        if secret_letter == letter:
            return True
    return False


def already_guessed(letter, guesses):
    for guess in guesses:
        if letter == guess:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    letter_check = False
    hangman_word = ""
    for secret_letter in secret_word:
        for guess_letter in guesses:
            if secret_letter == guess_letter:
                letter_check = True
        if letter_check:
            hangman_word = hangman_word + secret_letter + " "
        if not letter_check:
            hangman_word = hangman_word + "_" + " "
        letter_check = False
        # Guess Letter END
    # Secret Letter END
    hangman_word = hangman_word.strip()
    return hangman_word


def won(guessed):
    for letter in guessed:
        if letter == "_":
            return False
    return True


# Initializes and draws the gallows
def create_gallows(win):
    # Gallows Lines
    base_line = Line(Point(150, 450), Point(350, 450))
    beam_line = Line(Point(300, 450), Point(300, 75))
    top_beam_line = Line(Point(150, 75), Point(300, 75))
    noose = Line(Point(150, 75), Point(150, 125))

    # Drawing Gallows Lines
    base_line.draw(win)
    beam_line.draw(win)
    top_beam_line.draw(win)
    noose.draw(win)


# Initializes the individual parts of the hangman
def hangman_additions():
    head = Circle(Point(150, 155), 30)
    body = Line(Point(150, 185), Point(150, 325))
    right_leg = Line(Point(150, 325), Point(200, 400))
    left_leg = Line(Point(150, 325), Point(100, 400))
    right_arm = Line(Point(150, 210), Point(210, 265))
    left_arm = Line(Point(150, 210), Point(90, 265))
    return [head, body, right_leg, left_leg, right_arm, left_arm]


def play_graphics(secret_word):
    win = GraphWin("Hangman", 600, 600)

    # Instructions
    instructions_text = Text(Point(225, 550), "Guess a letter: ")
    guess_entry = Entry(Point(300, 550), 3)
    click_text = Text(Point(450, 550), "Click to submit letter")
    instructions_text.draw(win)
    guess_entry.draw(win)
    click_text.draw(win)

    # Texts
    guesses_text = Text(Point(450, 100), "")
    guesses_text.draw(win)
    hidden_word_text = Text(Point(300, 500), "")
    hidden_word_text.draw(win)
    results_text = Text(Point(300, 25), "")

    create_gallows(win)
    hangman_parts_list = hangman_additions()

    # GAME
    guessed = []
    guesses_remaining = 6
    guess = ""
    playing = True
    winner = False
    hangman_index = 0

    while playing:
        guesses_text.setText(guessed)
        hidden_word_text.setText(make_hidden_secret(secret_word, guessed))
        win.getMouse()
        guess = guess_entry.getText()

        if not already_guessed(guess, guessed):
            guessed.append(guess)
            if not letter_in_secret_word(guess, secret_word):
                guesses_remaining = guesses_remaining - 1
                hangman_parts_list[hangman_index].draw(win)
                hangman_index = hangman_index + 1
        if not guesses_remaining:
            playing = False
        if won(make_hidden_secret(secret_word, guessed)):
            playing = False
            winner = True
    # END while not game_over

    if winner:
        hidden_word_text.setText(make_hidden_secret(secret_word, guessed))
        results_text.setText("Congratulations, you are a winner!"
                             "\nSecret Word: " + secret_word)
    else:
        results_text.setText("Sorry, you did not guess the word within the number of tries."
                             "\nThe secret word was " + secret_word + ".")

    guesses_text.setText(guessed)
    results_text.draw(win)
    click_text.setText("Click to close")
    instructions_text.undraw()
    guess_entry.undraw()
    win.getMouse()
    win.close()


def play_command_line(secret_word):
    guessed = []
    guesses_remaining = 6
    guess = ""
    playing = True
    winner = False
    print("Welcome to Hangman!")

    while playing:
        print("\nAlready Guessed:", guessed)
        print("Guesses Remaining:", guesses_remaining)
        print(make_hidden_secret(secret_word, guessed))
        guess = input("Guess a Letter: ")

        if not already_guessed(guess, guessed):
            guessed.append(guess)
            if not letter_in_secret_word(guess, secret_word):
                guesses_remaining = guesses_remaining - 1
        if not guesses_remaining:
            playing = False
        if won(make_hidden_secret(secret_word, guessed)):
            playing = False
            winner = True
    # END while not game_over

    if winner:
        print(make_hidden_secret(secret_word, guessed))
        print("\nCongratulations, you are a winner!")
        print("Secret Word: " + secret_word)
    else:
        print("\nSorry, you did not guess the word within the number of tries.")
        print("The secret word was " + secret_word + ".")


if __name__ == '__main__':
    pass
    # play_command_line(get_random_word(get_words("words.txt")))
    # play_graphics(get_random_word(get_words("words.txt")))
