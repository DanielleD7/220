"""
Name: Danielle Di Pace
lab12.py

Problem: Various functions using while loops, lists, and numbers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(value_list, value):
    found = False
    count = 0
    while count < len(value_list):
        # Checks if the value matches and if it has not already been found
        if value_list[count] == value and not found:
            value_list.remove(value)
            value_list.insert(count, "Danielle")
            found = True
        count += 1
    # while loop END


def good_input():
    input_good = False
    user_input = eval(input("Enter a value between 1 and 10 (Inclusive): "))

    while not input_good:
        if 10 >= user_input >= 1:
            input_good = True

        if not input_good:
            if user_input > 10:
                print("\nYou input is greater than 10, please try again.")
            if user_input < 1:
                print("\nYou input is less than 1, please try again.")
            user_input = eval(input("Enter a value between 1 and 10 (Inclusive): "))
    # while loop END
    return user_input


def num_digits():
    user_input = eval(input("Enter a number (Enter a 0 or a negative number to exit): "))
    digit_count = 0

    while user_input > 0:
        digit_count = 0

        while user_input > 0:
            user_input = user_input // 10
            digit_count += 1
        # nested while loop END

        print("The number of digits in your number is", digit_count)
        user_input = eval(input("\nEnter a number (Enter a 0 or a negative number to exit): "))
    # while loop END


def hi_lo_game():
    secret_number = randint(1, 100)
    guesses = 0
    playing = True
    win = False
    user_guess = 0

    while playing:
        user_guess = eval(input("Enter a number to guess: "))
        guesses += 1

        if user_guess > secret_number:
            print("Your number is too high.")
        elif user_guess < secret_number:
            print("Your number is too low.")
        else:
            win = True
            playing = False

        if guesses == 7 and not win:
            playing = False
    # while loop END

    if win:
        print("Congratulations! You won in {} guesses!".format(guesses))
    else:
        print("Sorry, you lose. The number was {}".format(secret_number))
