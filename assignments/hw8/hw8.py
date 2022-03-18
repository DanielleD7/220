"""
Name: Danielle Di Pace
hw8.py

Problem: Various functions to manipulate integers, strings, and lists. These functions are then called
by another function to calculate the sum of squares. Other functions using if statements to determine
a person's weight class, if a year is a leap year, and if two circles overlap.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import GraphWin, Point, Text, Circle


def add_ten(nums):
    for index in range(len(nums)):
        nums[index] = nums[index] + 10


def square_each(nums):
    for index in range(len(nums)):
        nums[index] = (nums[index] ** 2)


def sum_list(nums):
    total = 0
    for num in nums:
        total = total + num
    return total


def to_numbers(nums):
    for index in range(len(nums)):
        nums[index] = eval(nums[index])


def sum_of_squares(nums):
    num_list = []
    sum_sqr_list = []

    for string_nums in nums:
        num_list = string_nums.split(", ")
        to_numbers(num_list)
        square_each(num_list)
        sum_sqr_list.append(sum_list(num_list))

    return sum_sqr_list


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    return False


def leap_year(year):
    if year % 400 == 0:
        return True
    if (year % 4 == 0) and (not year % 100 == 0):
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    # Circle One
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    # Circle Two
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_two = Circle(center, radius)
    circle_two.setFill("light green")
    circle_two.draw(win)

    if did_overlap(circle_one, circle_two):
        message = Text(Point(width / 2, height / 3), "The circles overlap")
    else:
        message = Text(Point(width / 2, height / 3), "The circles do not overlap")

    close_message = Text(Point(width / 2, (height / 3) - 1), "Click again to close")

    message.draw(win)
    close_message.draw(win)
    win.getMouse()


def did_overlap(circle_one, circle_two):
    distance = (circle_two.getCenter().getX() - circle_one.getCenter().getX()) ** 2
    distance = distance + ((circle_two.getCenter().getY() - circle_one.getCenter().getY()) ** 2)
    distance = math.sqrt(distance)
    radius_sum = circle_one.getRadius() + circle_two.getRadius()

    if distance <= radius_sum:
        return True
    return False


if __name__ == '__main__':
    pass
