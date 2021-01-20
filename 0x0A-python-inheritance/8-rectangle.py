#!/usr/bin/python3
"""
Implementing a new class called Rectangle
"""

class Rectangle(BaseGeometry):
    '''
    Class Rectangle inheriting BaseGeometry class attributes
    '''
    def __init__(self, width, height):
        '''
        Initializing Rectangle class
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
