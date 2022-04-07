"""
Name: Danielle Di Pace
face.py

Problem: A face class that allows the creation of a graphics face with methods to change expressions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Circle, Line, Polygon


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_size = 0.8 * self.head.getRadius()
        mouth_off = self.head.getRadius() / 2.0

        point_left = self.head.getCenter()
        point_left.move(-mouth_size / 2, mouth_off)

        point_right = self.head.getCenter()
        point_right.move(mouth_size / 2, mouth_off)

        point_center = self.head.getCenter()
        point_center.move(0, self.head.getRadius() / 1.3)

        self.mouth.undraw()
        self.mouth = Polygon(point_left, point_right, point_center)
        self.mouth.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        self.mouth = Circle(self.head.getCenter(), (0.15 * self.head.getRadius()))
        self.mouth.move(0, 1.5 * self.head.getRadius() / 3)
        self.mouth.draw(self.window)

    def wink(self):
        point_left = self.left_eye.getCenter()
        point_left.move(-self.left_eye.getRadius(), 0)

        point_right = self.left_eye.getCenter()
        point_right.move(self.left_eye.getRadius(), 0)

        self.left_eye.undraw()
        self.left_eye = Line(point_left, point_right)
        self.left_eye.draw(self.window)

        self.smile()
