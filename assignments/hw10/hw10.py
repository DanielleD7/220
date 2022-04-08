"""
Name: Danielle Di Pace
hw10.py

Problem: Various functions using loops for calculations, creating sequences, and a face graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(number):
    count = 0
    fib_num_1 = 1
    fib_num_2 = 1
    fib_num_final = 0

    if number < 1:
        return None
    if number < 3:
        return 1

    while count < number - 2:
        fib_num_final = fib_num_1 + fib_num_2
        fib_num_1 = fib_num_2
        fib_num_2 = fib_num_final
        count += 1
    return fib_num_final


def double_investment(principle, rate):
    amount = principle
    years = 0

    while amount < (principle * 2):
        amount = amount * (1 + rate)
        years = years + 1
    return years


def syracuse(number):
    syracuse_list = [number]

    while number != 1:
        # Even
        if number % 2 == 0:
            number /= 2
        # Odd
        else:
            number = (3 * number) + 1
        syracuse_list.append(number)
    # while loop END

    return syracuse_list


def goldbach(number):
    prime_numbers = []
    number_prime_sum = []
    # Even
    if number % 2 == 0:
        num = 1
        while num < (number + 1):
            if is_prime(num):
                prime_numbers.append(num)
            num += 1

        # Compares each prime number to find a sum matching the number
        num_1 = 0
        while num_1 < len(prime_numbers):
            num_2 = 0
            while num_2 < len(prime_numbers):
                if prime_numbers[num_1] + prime_numbers[num_2] == number:
                    number_prime_sum.append([prime_numbers[num_1], prime_numbers[num_2]])
                num_2 += 1
            # while loop END
            num_1 += 1
        # while loop END
        return number_prime_sum[0]
    return None


def is_prime(number):
    prime = True
    if number >= 2:
        num = 2
        while num < number:
            if number % num == 0:
                prime = False
            num += 1
        # while loop END
    else:
        prime = False
    return prime


if __name__ == '__main__':
    pass
