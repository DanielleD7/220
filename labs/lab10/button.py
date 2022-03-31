"""
Name: Danielle Di Pace
button.py

Problem: A Button class that creates a shape with a text label that behaves like a button.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

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

    def color_button(self, color):
        self.shape.setFill(color)

