"""
Name: Danielle Di Pace
hw1.py

Problem: Various functions that use the user's input to complete calculations
and display the calculated results to the user.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shot_percent = (shots_made / total_shots) * 100
    print("Shooting Percentage:", shot_percent, "%")


def coffee():
    coffee_cost = 10.50
    shipping_rate = 0.86
    shipping_flat = 1.50
    pounds = eval(input("How many pounds of coffee would you like? "))
    order_total = (coffee_cost * pounds) + (shipping_rate * pounds) + shipping_flat
    print("Your total is:", order_total)


def kilometers_to_miles():
    km_per_mile = 1.61
    km_traveled = eval(input("How many kilometers did you travel? "))
    miles = km_traveled / km_per_mile
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
