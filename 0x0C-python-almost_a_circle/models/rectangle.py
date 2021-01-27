#!/usr/bin/python3
'''Creating class Rectangle with some inherits from Base class'''


from models.base import Base


class Rectangle(Base):
    '''
    Defining class Rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initiating class Rectangle
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
        Definig getter of width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Defining setter of width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Defining Getter of height
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        Defining getter of height
        '''
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        '''
        Defining getter of x
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''
        defining setter of x
        '''
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        '''
        Defining getter of y
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''
        Defining setter of y
        '''
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''
        Return the area value of the Rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Prints the STDOUT of the Rectangle with #
        '''
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        '''
        Override the __str__ method
        '''
        str1 = '(' + str(self.id) + ') ' + str(self.__x) + '/'
        str2 = str(self.__y) + ' - ' + str(self.__width)
        return "[Rectangle] " + str1 + str2 + "/" + str(self.__height)
