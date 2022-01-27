"""
Name: Danielle Di Pace
lab2.py

Problem: Calculates the Root-Mean-Square, Harmonic Mean, and the Geometric Mean
based on the user inputs for the number of values and their individual values.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


# Calculates the Root-Mean-Square, Harmonic Mean, and the Geometric Mean
# based on the user's input
def means():
    number_of_values = eval(input("Enter the number of values you want: "))

    # Increment Accumulators
    root_mean_square = 0
    harmonic_mean = 0
    geometric_mean = 1

    for i in range(number_of_values):
        value = eval(input("Enter the value: "))

        # Increment Accumulators
        root_mean_square += value**2
        harmonic_mean += (1/value)
        geometric_mean *= value
    # for loop END

    # Root-Mean-Square Calculations
    root_mean_square = math.sqrt(root_mean_square / number_of_values)

    # Harmonic Mean Calculations
    harmonic_mean = number_of_values/harmonic_mean

    # Geometric Mean Calculations
    geometric_mean = geometric_mean**(1/number_of_values)

    # Mean outputs
    print("\nRoot-Mean-Square:", round(root_mean_square, 3))
    print("Harmonic Mean:", round(harmonic_mean, 3))
    print("Geometric Mean:", round(geometric_mean, 3))


means()
