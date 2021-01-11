#!/usr/bin/python3
'''
Defining a Rectangle
'''


class Rectangle:
    """
    Class representing a Rectangle
    Attributes:
    - width: integer that meassures the width of the rectangle
    - height: Integer that meassures the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Return Private Variable width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Check for TypeError & ValueError, then
        setting the private variables
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Return Private Variable height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Check for TypeError & ValueError, then
        setting the private variable
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
