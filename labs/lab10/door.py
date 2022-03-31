"""
Name: Danielle Di Pace
door.py

Problem: A Door class that creates a color changing door based on whether it is open or not.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if self.shape.getP1().getX() <= point.getX() <= self.shape.getP2().getX():
            if self.shape.getP1().getY() <= point.getY() <= self.shape.getP2().getY():
                return True
        return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True

    def set_secret(self, secret):
        self.secret = secret

