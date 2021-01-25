#!/usr/bin/python3
'''This is the BASE class of all other classes'''

class Base:
    '''
    Manage id attribute in all future classes to avoid duplicating the same code
    '''
    __nb_objects = 0

    def __init__(self, id=None):


        if id is None:
            Base.__nb_objects + 1
            id = Base.__nb_objects

        self.id = id
