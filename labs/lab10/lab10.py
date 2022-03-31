"""
Name: Danielle Di Pace
lab10.py

Problem: Using graphics to display an exit button created by the Button class and a color changing
door with the Door class. When the user clicks inside the exit button, the window closes.
If the user clicks inside the door it changes color and its text label relating to being open or closed.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from button import *
from door import *


def main():
    win = GraphWin("Door Game", 600, 600)
    win_open = True
    click = None
    door_count = 0

    # Exit Button
    exit_button_shape = Rectangle(Point(175, 25), Point(425, 150))
    exit_label = "Exit"
    exit_button = Button(exit_button_shape, exit_label)
    exit_button.draw(win)

    # Door
    door_shape = Rectangle(Point(175, 175), Point(425, 600))
    door_label = "Closed"
    door = Door(door_shape, door_label)
    door.draw(win)
    door.color_door("dark red")

    while win_open:
        click = win.getMouse()

        if exit_button.is_clicked(click):
            win_open = False
        if door.is_clicked(click):
            door_count = door_count + 1

            if door_count % 2:
                door.open("white", "Open")
            else:
                door.close("dark red", "Closed")
    # END while win_open loop
    win.close()


main()
