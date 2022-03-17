"""
Name: Danielle Di Pace
lab8.py

Problem: Animate two circles with randomly generated colors.
When the circles collide with the edges of the window or with each other, they will bounce off of it

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from random import randint
import math


# Generates a random number based off of the passed value
def get_random(move_amount):
    return randint(-move_amount, +move_amount)


# Checks to see if two objects collide with each other
def did_collide(ball, ball2):
    distance = ((ball2.getCenter().getX() - ball.getCenter().getX()) ** 2)
    distance = distance + ((ball2.getCenter().getY() - ball.getCenter().getY()) ** 2)
    distance = math.sqrt(distance)

    radius_sum = ball.getRadius() + ball2.getRadius()

    if distance <= radius_sum:
        return True
    return False


# Checks if the object hits the top or bottom side of the window
def hit_vertical(ball, win):
    if (ball.getCenter().getY() + ball.getRadius()) >= win.getHeight():
        return True
    elif (ball.getCenter().getY() - ball.getRadius()) <= 0:
        return True
    else:
        return False


# Checks if the object hits the left or right side of the window
def hit_horizontal(ball, win):
    if (ball.getCenter().getX() + ball.getRadius()) >= win.getWidth():
        return True
    elif (ball.getCenter().getX() - ball.getRadius()) <= 0:
        return True
    else:
        return False


# Returns a random rgb number in a list, 3 numbers total
def get_random_color():
    rgb_code_list = []
    for index in range(3):
        rgb_code_list.append(randint(0, 255))

    return rgb_code_list


def get_random_direction(radius):
    ball_direction = get_random(radius)

    if ball_direction > 0:
        ball_direction = 1
    elif ball_direction < 0:
        ball_direction = -1
    else:
        ball_direction = 0

    return ball_direction


def bumper():
    win = GraphWin("Bumper", 500, 500)
    radius = 30

    # BALL
    # Creates random x and y values for the circle's point
    # Set up so the circle will not be touching or going past the window on initial creation
    x_value = randint(radius + 1, win.getWidth() - (radius + 1))
    y_value = randint(radius + 1, win.getHeight() - (radius + 1))
    ball = Circle(Point(x_value, y_value), radius)

    # Random rgb values set for ball's fill and outline
    rgb_code_list = get_random_color()
    ball.setFill(color_rgb(rgb_code_list[0], rgb_code_list[1], rgb_code_list[2]))
    rgb_code_list = get_random_color()
    ball.setOutline(color_rgb(rgb_code_list[0], rgb_code_list[1], rgb_code_list[2]))

    # BALL 2
    # Creates random x and y values for the circle's point
    # Set up so the circle will not be touching or going past the window on initial creation
    x_value = randint(radius + 1, win.getWidth() - (radius + 1))
    y_value = randint(radius + 1, win.getHeight() - (radius + 1))
    ball2 = Circle(Point(x_value, y_value), radius)

    # Random rgb values set for ball2's fill and outline
    rgb_code_list = get_random_color()
    ball2.setFill(color_rgb(rgb_code_list[0], rgb_code_list[1], rgb_code_list[2]))
    rgb_code_list = get_random_color()
    ball2.setOutline(color_rgb(rgb_code_list[0], rgb_code_list[1], rgb_code_list[2]))

    # Drawing
    ball.draw(win)
    ball2.draw(win)

    # Initial Direction
    # The integer passed to get_random does not matter much
    # But the bigger the value, the less likely it will hit zero
    ball_direction = [get_random_direction(radius), get_random_direction(radius)]
    ball2_direction = [get_random_direction(radius), get_random_direction(radius)]

    # Loops the bumper animation until the user clicks the window
    while win.checkMouse() is None:
        # Moves the balls
        ball.move(ball_direction[0], ball_direction[1])
        ball2.move(ball2_direction[0], ball2_direction[1])

        # Checks if the ball hits the top or bottom side of the window
        if hit_vertical(ball, win):
            ball_direction[1] = -ball_direction[1]
        if hit_vertical(ball2, win):
            ball2_direction[1] = -ball2_direction[1]

        # Checks if the ball hits the left or right side of the window
        if hit_horizontal(ball, win):
            ball_direction[0] = -ball_direction[0]
        if hit_horizontal(ball2, win):
            ball2_direction[0] = -ball2_direction[0]
        # Checks if the balls collide with each other
        if did_collide(ball, ball2):
            ball_direction[0] = -ball_direction[0]
            ball_direction[1] = -ball_direction[1]
            ball2_direction[0] = -ball2_direction[0]
            ball2_direction[1] = -ball2_direction[1]

        time.sleep(0.001)
    # END while loop animation
    win.close()


bumper()
