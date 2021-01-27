#!/usr/bin/python3
'''Class Square and import'''


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Creating Square class from Rectangle class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(
           self.id, self.x, self.y, self.width))

    @property
    def size(self):
        '''
        Defining getter of size of the square
        '''
        return self.width

    @size.setter
    def size(self, value):
        super().__setattr__('width', value)
        super().__setattr__('height', value)

    def update(self, *args, **kwargs):
        '''
        Updating the values of the instances
        '''
        list1 = ["id", "size", "x", "y"]
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, list1[arg], args[arg])

    def to_dictionary(self):
        '''
        Representation of Dictionary
        '''
        return dict(x=self.x, y=self.y, id=self.id, size=self.width)
