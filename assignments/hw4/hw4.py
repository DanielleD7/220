"""
Name: Danielle Di Pace
hw4.py

Problem: Creating varius shapes base on the user's input using the graphics object and calculations
and calculating an approximation of pi.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import GraphWin, Point, Text, Rectangle, Circle


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for _ in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of square

        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        # creates a new square to be drawn and moved
        new_shape = shape.clone()
        new_shape.draw(win)
        new_shape.move(change_x, change_y)
    # for loop END

    click_message = Text(Point(200, 200), "Click again to close")
    click_message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win_width = 400
    win_height = 400
    win = GraphWin("Rectangle", win_width, win_height)

    message = Text(Point(200, 350), "Click twice to add two points to create a rectangle.")
    message.draw(win)

    click1 = win.getMouse()
    click2 = win.getMouse()

    # Creates a rectangle with mouse clicks
    rec_shape = Rectangle(Point(click1.getX(), click1.getY()), Point(click2.getX(), click2.getY()))
    rec_shape.setFill("green")
    rec_shape.draw(win)

    # Changes message and undraws then draw to bring it in front of the rectangle
    message.setText("Click again to close")
    message.move(0, -150)
    message.undraw()
    message.draw(win)

    # Height, width, parameter, and area calculations
    rectangle_height = abs(click2.getY() - click1.getY())
    rectangle_width = abs(click2.getX() - click1.getX())
    parameter = (rectangle_height * 2) + (rectangle_width * 2)
    area = rectangle_height * rectangle_width

    # Parameter and Area Display
    parameter_text = Text(Point(170, 350), "Parameter: ")
    parameter_number_text = Text(Point(235, 350), parameter)
    area_text = Text(Point(170, 375), "Area: ")
    area_number_text = Text(Point(230, 375), area)

    parameter_text.draw(win)
    parameter_number_text.draw(win)
    area_text.draw(win)
    area_number_text.draw(win)

    win.getMouse()
    win.close()


def circle():
    win_width = 400
    win_height = 400
    win = GraphWin("Circle", win_width, win_height)

    # Getting the center
    message = Text(Point(200, 350), "Click once to mark the center of the circle.")
    message.draw(win)
    center = win.getMouse()

    # Getting a circumference point and calculating the radius
    message.setText("Click for a point on the circumference.")
    cir_point = win.getMouse()
    radius = (cir_point.getX() - center.getX()) ** 2 + (cir_point.getY() - center.getY()) ** 2
    radius = math.sqrt(radius)

    # Creating the circle
    circle_shape = Circle(center, radius)
    circle_shape.setFill("LightSkyBlue")
    circle_shape.draw(win)

    # Redraws the message, so it will be on top of the circle
    message.setText("Click again to close")
    message.move(0, -150)
    message.undraw()
    message.draw(win)

    # Displaying the radius
    radius_text = Text(Point(120, 375), "Radius: ")
    radius_number_text = Text(Point(230, 375), radius)

    radius_text.draw(win)
    radius_number_text.draw(win)

    win.getMouse()


def pi2():
    terms = eval(input("Enter the number of terms to sum: "))
    numerator = 4
    denominator = 1
    pi_approximation = 0

    for _ in range(terms // 2):
        value1 = (numerator / denominator)
        denominator = denominator + 2
        value2 = (numerator / denominator)

        pi_approximation = pi_approximation + (value1 - value2)
        denominator = denominator + 2
    # Even for loop END

    for _ in range(terms % 2):
        pi_approximation = pi_approximation + (numerator / denominator)
    # Odd for loop END

    accuracy = abs(math.pi - pi_approximation)
    print("Pi Approximation:", pi_approximation)
    print("Accuracy:", accuracy)


if __name__ == '__main__':
    pass
