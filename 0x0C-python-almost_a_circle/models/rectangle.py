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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
                if not isinstance(width, int):
                    raise TypeError("width must be an integer")
                if width <= 0:
                    raise ValueError("width must be > 0")
