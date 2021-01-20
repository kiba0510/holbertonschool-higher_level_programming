#!/usr/bin/python3
"""
Implementing a new class called Rectangle
"""


class BaseGeometry:
    '''BaseGeometry class'''
    def area(self):
        """
        Function that calculates the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        CHeck for validating an integer
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        '''
        Defining area methd
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Defining str method
        '''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    '''
    Square class with inheritance of Rectangle class attributes
    '''
    def __init__(self, size):
        ''' initialize the class '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' define area method '''
        return self.__size ** 2

    def __str__(self):
        ''' define str method '''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
