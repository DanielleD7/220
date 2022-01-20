"""
Name: Danielle Di Pace
lab1.py

Problem: Calculates the user's monthly interest charge using the user's inputted account data.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def monthly_interest():

    # Acquire user input on their account information
    annual_interest_rate = eval(input("Enter your annual interest rate: ")) / 100
    days_in_cycle = eval(input("Enter the number of days in your billing cycle: "))
    net_balance = eval(input("Enter your previous net balance: "))
    payment = eval(input("Enter your payment amount: "))
    payment_day = eval(input("Enter the day you made the payment: "))

    # Calculates the user's monthly interest change using their inputted values
    average_daily_balance = (((net_balance * days_in_cycle) - (payment * (days_in_cycle - payment_day)))/days_in_cycle)
    monthly_interest_charge = average_daily_balance * (annual_interest_rate / 12)

    print("Here is your monthly interest charge: $", round(monthly_interest_charge, 2))


monthly_interest()

