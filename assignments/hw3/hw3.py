"""
Name: Danielle Di Pace
hw3.py

Problem: Calculates the result of varius mathematical problems using for loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    number_of_grades = eval(input("Enter the number of grades you want to enter: "))
    grade = 0
    for _ in range(number_of_grades):
        grade = grade + eval(input("Enter grade: "))
    # for loop END

    grade_average = grade / number_of_grades
    print("\nGrade average:", grade_average)


def tip_jar():
    number_of_people = 5
    tips = 0

    for _ in range(number_of_people):
        tips = tips + eval(input("How much would you like to donate? "))
    # for loop END

    print("\nTotal tips: $", round(tips, 20))


def newton():
    number_to_be_sqrt = eval(input("What number do you want to square root? "))
    approx_count = eval(input("How many times should we improve the approximation? "))
    approx_square_root = number_to_be_sqrt

    for _ in range(approx_count):
        approx_square_root = (approx_square_root + (number_to_be_sqrt / approx_square_root)) / 2

    print("The square root is approximately", approx_square_root)


def sequence():
    terms = eval(input("How many terms would you like? "))
    # loop_1 = terms // 2
    # loop_2 = terms % 2
    sequence_num = -1

    for _ in range(terms // 2):
        sequence_num = sequence_num + 2
        print(sequence_num, sequence_num, end=" ")
    # even for loop END
    for _ in range(terms % 2):
        sequence_num = sequence_num + 2
        print(sequence_num, end=" ")
    # odd for loop END


def pi():
    terms = eval(input("How many terms in the series? "))

    numerator = 1
    numerator_count = 0

    denominator = 1
    denominator_count = 1

    # Numerator
    for _ in range(terms // 2):
        numerator_count = numerator_count + 2
        numerator = numerator * (numerator_count * numerator_count)
        # print("Loop1: ", numerator)
    # even - numerator for loop END

    for _ in range(terms % 2):
        # print(numerator)
        numerator_count = numerator_count + 2
        numerator = numerator * numerator_count
        # print("Loop2: ", numerator)
    # odd - numerator for loop END

    # print("Numerator:", numerator)
    # print()

    # Denominator
    for _ in range((terms - 1) // 2):
        denominator_count = denominator_count + 2
        denominator = denominator * (denominator_count * denominator_count)
        # print("Loop1: ", denominator)
    # even - denominator for loop END

    for _ in range((terms - 1) % 2):
        # print(denominator)
        denominator_count = denominator_count + 2
        denominator = denominator * denominator_count
        # print("Loop2: ", denominator)
    # odd - denominator for loop END

    # print("Denominator:", denominator)

    pi_approximation = (numerator / denominator) * 2

    print("Pi approximation:", pi_approximation)


if __name__ == '__main__':
    pass
