#!/usr/bin/python3
"""
Square Module - Use when you need to print a square
"""


class Square:
    """
    Class defining the size of a square
    """
    def __init__(self, size=0):
        """
        Initialization of instanced attribute
        Args:
        size: The size of a square, it must be an integer and >= 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
