#!/usr/bin/python3
'''This is the BASE class of all other classes'''

class Base:
    '''
    Manage id attribute in all future classes to avoid duplicating the same code
    '''
    

    def __init__(self, id=None):
       
        __nb_object = 0

        if id is not None:
            self.id = id
        else:
            self.id = __nb_objects + 1
