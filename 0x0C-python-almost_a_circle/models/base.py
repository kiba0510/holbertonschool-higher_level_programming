#!/usr/bin/python3
'''This is the BASE class of all other classes'''

class Base:
    '''
    Manage id attribute in all future classes to avoid duplicating the same code
    '''
import json
import csv
import turtle

__nb_objects = 0

def __init__(self, id=None):
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_object
