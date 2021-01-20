#!/usr/bin/python3
"""
Defining a geometry class
"""


class BaseGeometry:
    def area(self):
        """
        Function that calculates the area
        """
        raise Exception("area() is not implemented")
