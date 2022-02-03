"""
Name: Danielle Di Pace
lab3.py

Problem: Uses the user's input of the number of roads, days surveyed for each road, and the number of
vehicles traveled on each road per day to calculate the average number of vehicles traveling for each
road, the total number vehicles that have traveled on all roads, and the average number of vehicles per road.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    number_of_roads = eval(input("How many roads were surveyed? "))
    total_vehicles = 0

    # Loops through each road
    for road in range(1, number_of_roads + 1):
        print("How many days was road", road, "surveyed?", end=" ")
        days_surveyed = eval(input(""))
        vehicle_count = 0

        # Loops through each day per road
        for day in range(1, days_surveyed + 1):
            print("\tHow many vehicles traveled on day", day, "?", end=" ")
            vehicle_count += eval(input(""))
        # day for loop END

        total_vehicles += vehicle_count
        print("Road", road, "average vehicles per day:", round(vehicle_count / days_surveyed, 1))
    # road for loop END

    print("Total number of vehicles traveled on all roads:", total_vehicles)
    print("Average number of vehicles per road:", round(total_vehicles / number_of_roads, 2))


traffic()
