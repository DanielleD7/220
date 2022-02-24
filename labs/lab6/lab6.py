"""
Name: Danielle Di Pace
lab6.py

Problem: Encode the user's message with their key using the Vigenere Cipher using a graphical display.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def vigenere():
    win = GraphWin("Vigenere", 600, 400)

    # Text
    message_text = Text(Point(100, 75), "Message to code")
    key_text = Text(Point(100, 125), "Enter Keyword")
    encode_text_button = Text(Point(300, 200), "Encode")
    result_text = Text(Point(300, 250), "Resulting Message")
    close_text = Text(Point(300, 350), "Click Anywhere to Close Window")

    # Entry Boxes
    message_entry = Entry(Point(375, 75), 40)
    key_entry = Entry(Point(285, 125), 20)

    # Button Box
    button_box = Rectangle(Point(250, 175), Point(350, 225))

    # Initial Draws
    message_text.draw(win)
    message_entry.draw(win)
    key_text.draw(win)
    key_entry.draw(win)
    encode_text_button.draw(win)
    button_box.draw(win)

    # Waiting for mouse click after values are inputted
    win.getMouse()

    # Making message and key all uppercase and removing all spaces
    message = message_entry.getText().upper().replace(" ", "")
    key = key_entry.getText().upper().replace(" ", "")
    key_length = len(key)

    encoded_message = ""
    count = 0

    # Vigenere
    for letter in message:
        message_letter_code = (ord(letter) - 65)
        key_letter_code = (ord(key[count % key_length]) - 65)

        new_code = message_letter_code + key_letter_code
        new_code = (new_code % 26) + 65

        encoded_message = encoded_message + chr(new_code)

        count = count + 1
    # Vigenere loop END

    encoded_message_text = Text(Point(300, 275), encoded_message)

    # Draw After Vigenere
    encode_text_button.undraw()
    button_box.undraw()
    result_text.draw(win)
    encoded_message_text.draw(win)
    close_text.draw(win)

    # Closing
    win.getMouse()
    win.close()


vigenere()
