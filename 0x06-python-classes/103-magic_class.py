#!/usr/bin/python3
""" Class form python bytecode for magic objects"""


import math


class MagicClass:

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self._radius = radius
        self._circumference = None

    def area(self):
        return self._radius ** 2 * math.pi

    def circumference(self):
        if self._circumference is None:
            self._circumference = math.pi * 2 * self._radius
        return self._circumference
