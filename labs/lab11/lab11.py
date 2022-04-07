"""
Name: Danielle Di Pace
lab11.py

Problem: A three door game where the user can click on a door to see if they win.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from random import randint
from lab10.button import Button
from lab10.door import Door


def three_door_game():
    window = GraphWin("Three Door Game", 700, 700)
    window.setBackground("cornflower blue")
    doors = []
    door_index = -1
    win_score = 0
    lose_score = 0
    mouse_click = Point(1, 1)
    win = False

    # Texts
    instruction_text = Text(Point(350, 650), "Click to guess which is the secret door!")
    result_text = Text(Point(350, 150), "I have a secret door")

    # Score Box
    win_box_text = Text(Point(60, 50), "Wins")
    lose_box_text = Text(Point(120, 50), "Losses")
    win_score_num_text = Text(Point(60, 85), win_score)
    lose_score_num_text = Text(Point(120, 85), lose_score)
    win_box = Rectangle(Point(30, 60), Point(90, 110))
    lose_box = Rectangle(Point(90, 60), Point(150, 110))

    # Doors
    door_1 = Door(Rectangle(Point(80, 225), Point(205, 550)), "Door 1")
    door_1.color_door("saddle brown")
    door_2 = Door(Rectangle(Point(275, 225), Point(400, 550)), "Door 2")
    door_2.color_door("saddle brown")
    door_3 = Door(Rectangle(Point(465, 225), Point(590, 550)), "Door 3")
    door_3.color_door("saddle brown")

    # Adding the doors to a list
    doors.append(door_1)
    doors.append(door_2)
    doors.append(door_3)

    # Quit Button
    quit_button = Button(Rectangle(Point(550, 60), Point(650, 110)), "Quit")

    # Text and Button Draw
    instruction_text.draw(window)
    result_text.draw(window)
    quit_button.draw(window)

    # Score Box Draw
    win_box_text.draw(window)
    lose_box_text.draw(window)
    win_score_num_text.draw(window)
    lose_score_num_text.draw(window)
    win_box.draw(window)
    lose_box.draw(window)

    # Door Draw
    door_1.draw(window)
    door_2.draw(window)
    door_3.draw(window)

    # Check if the quit button was clicked
    while not quit_button.is_clicked(mouse_click):
        # Sets the secret door
        secret = randint(0, len(doors) - 1)
        doors[secret].set_secret(True)

        mouse_click = window.getMouse()

        # If the user did not click the quit button
        if not quit_button.is_clicked(mouse_click):
            # Finds the door the user clicked
            for index in range(0, len(doors)):
                if doors[index].is_clicked(mouse_click):
                    win = doors[index].is_secret()
                    door_index = index

            # Results
            if win:
                result_text.setText("You win!")
                doors[door_index].color_door("Green")
                win_score += 1
                win_score_num_text.setText(win_score)
            if not win and door_index > -1:
                result_text.setText("Sorry, incorrect!")
                doors[door_index].color_door("Crimson")
                lose_score += 1
                lose_score_num_text.setText(lose_score)

            # If the user had clicked on a door
            # It allows for another mouse click to reset the game or quit
            if door_index > -1:
                instruction_text.setText("Click anywhere to play again")
                mouse_click = window.getMouse()

            # Reset (Will be skipped if no doors are clicked)
            if not quit_button.is_clicked(mouse_click):
                # Text Reset
                instruction_text.setText("Click to guess which is the secret door!")
                result_text.setText("I have a secret door")

                # Game Reset
                doors[door_index].color_door("saddle brown")
                doors[secret].set_secret(False)
                win = False
                door_index = -1
    # while loop END
    window.close()


three_door_game()
