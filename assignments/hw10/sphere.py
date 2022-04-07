"""
Name: Danielle Di Pace
sphere.py

Problem: A sphere class that creates a sphere and calculates the surface area and volume.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


class Sphere:
    """
    Represents a sphere with a radius
    """
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)
