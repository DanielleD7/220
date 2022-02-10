"""
Name: Danielle Di Pace
lab4.py

Problem: Create a Valentine's Day greeting card of a heart with an animated arrow
         going through it and a message

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def greeting_card():

    # Window
    win = GraphWin("Happy Valentine's Day!", 700, 700)
    win.setBackground("Pink")

    # Valentine's Day Message
    val_message = Text(Point(350, 575), "Happy Valentine's Day!")
    val_message.setSize(25)
    val_message.setStyle("bold")
    val_message.setTextColor("Crimson")

    # Closing Message
    closing_message = Text(Point(350, 500), "Click to Close.")
    closing_message.setSize(15)

    # Heart Left
    heart_left = Circle(Point(275, 200), 75)
    heart_left.setFill("Crimson")
    heart_left.setOutline("Crimson")

    # Heart Right
    heart_right = Circle(Point(420, 200), 75)
    heart_right.setFill("Crimson")
    heart_right.setOutline("Crimson")

    # Heart Bottom
    heart_bottom = Polygon(Point(206, 230), Point(489, 230), Point(350, 425))
    heart_bottom.setFill("Crimson")
    heart_bottom.setOutline("Crimson")

    # Heart Center
    heart_center = Circle(Point(345, 260), 70)
    heart_center.setFill("Crimson")
    heart_center.setOutline("Crimson")

    # Arrow Base
    arrow_base = Polygon(Point(1200, 1060), Point(1210, 1045), Point(850, 810), Point(840, 825))
    arrow_base.setFill("Black")

    # Arrow Point
    arrow_point = Polygon(Point(870, 785), Point(820, 850), Point(793, 780))
    arrow_point.setFill("Black")

    # Drawing
    heart_left.draw(win)
    heart_right.draw(win)
    heart_bottom.draw(win)
    arrow_base.draw(win)
    arrow_point.draw(win)
    heart_center.draw(win)
    val_message.draw(win)

    # Animation for loop for the arrow base and head
    for i in range(10):
        arrow_base.move(-70, -70)
        arrow_point.move(-70, -70)
        time.sleep(0.05)
    # Animation for loop END

    # Closing
    time.sleep(0.6)
    closing_message.draw(win)
    win.getMouse()
    win.close()


greeting_card()
