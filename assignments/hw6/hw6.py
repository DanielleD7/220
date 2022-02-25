"""
Name: Danielle Di Pace
hw6.py

Problem: Formatting strings to print in different ways, encoding a message using unicode,
and returning calculated values from parameters.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    integer = eval(input("Enter an integer: "))
    print("That is ${:.2f}".format(integer))


def encode():
    message = input("Enter a message: ")
    key = eval(input("Enter a key: "))
    code = ""

    for letter in message:
        code = code + chr((ord(letter) + key))

    print(code)


def sphere_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


def sum_n(number):
    total = 0
    for num in range(1, number + 1):
        total = total + num

    return total


def sum_n_cubes(number):
    total = 0
    for num in range(1, number + 1):
        total = total + (num ** 3)

    return total


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")

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

    print(encoded_message)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
