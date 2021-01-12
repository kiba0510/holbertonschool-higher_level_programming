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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol

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

    def area(self):
        '''
        Calculates the area of the Rectangle
        '''
        return self.height * self.width

    def perimeter(self):
        '''
        Calculates the perimeter of the Rectangle
        '''
        if self.height == 0 or self.width == 0:
                return 0

        return (self.height + self.width) * 2

    def __str__(self):
        '''
        Returns the string representation of the Rectangle
        '''
        if self.height == 0 or self.width == 0:
            return ""
        psy = (str(self.print_symbol) * self.width + "\n") * self.height
        return psy[:-1:]

    def __repr__(self):
        '''
        Returns the representation of the Rectangle'''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        '''
        Deletes the Rectangle instance
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
