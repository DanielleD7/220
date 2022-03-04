"""
Name: Danielle Di Pace
encryption.py

Problem: Two methods of encrypting data passed to the function using a key

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def encode(message, key):
    code = ""

    for letter in message:
        code = code + chr((ord(letter) + key))

    return code


def encode_better(message, key):

    key_length = len(key)
    encoded_message = ""
    count = 0

    # Encoding Loop
    for letter in message:
        message_letter_code = (ord(letter) - 65)
        key_letter_code = (ord(key[count % key_length]) - 65)

        new_code = message_letter_code + key_letter_code
        new_code = (new_code % 58) + 65

        encoded_message = encoded_message + chr(new_code)

        count = count + 1
    # Encoding Loop END

    return encoded_message

