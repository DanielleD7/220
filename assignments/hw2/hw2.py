"""
Name: Danielle Di Pace
hw2.py

Problem: Various types of mathematical functions that utilize the user's input
to complete calculations and displays the result.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    three_sum = 0

    for i in range(1, (upper_bound // 3) + 1):
        three_sum = three_sum + (i * 3)

    print("Sum of threes is", three_sum)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print()


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))

    semi_perimeter = ((side_a + side_b + side_c) / 2)
    area = (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)
    area = math.sqrt(semi_perimeter * area)
    print("Area is:", area)


def sum_squares():
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    sum_of_squares = 0

    for i in range(lower_range, upper_range + 1):
        sum_of_squares = sum_of_squares + (i * i)

    print(round(sum_of_squares))


def power():
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    answer = base

    for _ in range(exponent - 1):
        answer = answer * base

    print(base, "^", exponent, "=", answer)


if __name__ == '__main__':
    pass
