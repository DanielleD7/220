"""
Name: Danielle Di Pace
lab5.py

Problem: Various functions that use the graphics library to create a triangle, change the color of a circle,
and create a stack of circles, alter strings and lists, and print out a sequence.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def triangle():
    win = GraphWin("Triangle", 500, 500)

    # Instructions
    instructions = Text(Point(250, 450), "Click three times to create points for a triangle.")
    close_message = Text(Point(250, 375), "Click to close.")
    instructions.draw(win)

    # Triangle Creation
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    triangle_shape = Polygon(Point(point1.getX(), point1.getY()), Point(point2.getX(), point2.getY()),
                             Point(point3.getX(), point3.getY()))
    triangle_shape.draw(win)

    # Calculations
    side_a = math.sqrt(((point2.getX() - point1.getX()) ** 2) + ((point2.getY() - point1.getY()) ** 2))
    side_b = math.sqrt(((point3.getX() - point2.getX()) ** 2) + ((point3.getY() - point2.getY()) ** 2))
    side_c = math.sqrt(((point1.getX() - point3.getX()) ** 2) + ((point1.getY() - point3.getY()) ** 2))

    parameter = side_a + side_b + side_c
    area = (side_a + side_b + side_c) / 2
    area = math.sqrt(area * (area - side_a) * (area - side_b) * (area - side_c))

    # Calculations Messages
    parameter_message = Text(Point(250, 425), "Parameter: " + str(round(parameter, 2)))
    area_message = Text(Point(250, 450), "Area: " + str(round(area, 2)))

    # Drawings
    instructions.undraw()
    parameter_message.draw(win)
    area_message.draw(win)
    close_message.draw(win)

    # Closing
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # Entry box for Red
    red_entry = Entry(Point(win_width / 2 + 10, win_height / 2 + 40), 6)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # Entry box for Green
    green_entry = red_entry.clone()
    green_entry.move(0, 30)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # Entry box for Blue
    blue_entry = red_entry.clone()
    blue_entry.move(0, 60)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_entry.draw(win)
    green_entry.draw(win)
    blue_entry.draw(win)

    # RGB Color Change Loop
    for _ in range(5):
        win.getMouse()
        red_color = int(red_entry.getText())
        green_color = int(green_entry.getText())
        blue_color = int(blue_entry.getText())
        shape.setFill(color_rgb(red_color, green_color, blue_color))
    # Color Change Loop END

    # Wait for another click to exit
    close_message = Text(Point(win_width / 2, win_height / 2 + 150), "Click to close.")
    close_message.draw(win)
    win.getMouse()
    win.close()


def process_string():
    word = input("Enter a word that is at least 5 characters long: ")
    print("First character: " + word[0])

    print("Last character: " + word[len(word) - 1])

    print("Characters in positions 2 - 5: " + word[1:5])

    print("First and last character: " + word[0] + word[len(word) - 1])

    print("First three characters repeated 10 times: " + word[0:3] * 10)

    print("Each character in their own line: ")
    for letter in word:
        print(letter)

    print("Number of characters: " + str(len(word)))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1] * 5
    print(x)

    x = [values[2], values[3], values[4]]
    print(x)

    x = [values[2], values[3], values[0]]
    print(x)

    x = [values[2], values[0], float(values[5])]
    print(x)

    x = values[0] + values[2] + float(values[5])
    print(x)

    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Enter the number of terms you want: "))
    sequence_sum = 0

    for i in range(0, terms):
        number = (((i % 3) + 2) + i % 3)
        print(number, end=" ")
        sequence_sum = sequence_sum + number

    print("\nSum:", sequence_sum)


def target():
    win = GraphWin("Target", 500, 500)
    close_message = Text(Point(250, 475), "Click to close.")

    center = Point(250, 250)
    radius = 50

    yellow_circle = Circle(center, radius)
    yellow_circle.setFill("yellow")

    red_circle = Circle(center, radius * 2)
    red_circle.setFill("red")

    blue_circle = Circle(center, radius * 3)
    blue_circle.setFill("blue")

    black_circle = Circle(center, radius * 4)
    black_circle.setFill("black")

    white_circle = Circle(center, radius * 5)
    white_circle.setFill("white")

    white_circle.draw(win)
    black_circle.draw(win)
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)
    close_message.draw(win)

    win.getMouse()
    win.close()
