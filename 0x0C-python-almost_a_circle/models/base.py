#!/usr/bin/python3
'''This is the BASE class of all other classes'''
import json


class Base:
    '''
    Manage id attribute in all future classes
    to avoid duplicating the same code
    '''
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Static method that returns JSON string representation
        '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_dictionaries):
        '''
        Writes the JSON string representation of list_objs to a file    
        '''
        file = "{}.json".format(cls.__name__)
        with open(file, 'w', encoding='UTF-8') as fname:
            emptylist = []
            if list_objs is not None:
                for obj in list_objs:
                    emptylist.append(cls.to_dictionary(obj))
                emptylist = Base.to_json_string(emptylist)
                file.write(str(emptylist))

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list of the JSON string representation json_string
        '''
        emptylist = []
        if json_string is None or not json_string:
            return emptylist
        else:
            aux = json.loads(json_string)
            return aux

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        name = cls.__name__ + '.json'
        emptylist = []
        list3 = []
        try:
            with open(name, mode='r', encoding='UTF8') as xfile:
                aux = xfile.read()
                emptylist = cls.from_json_string(aux)
                '''List of dictionaries'''
                for elem in emptylist:
                    aux2 = cls.create(**elem)
                    list3.append(aux2)
                return list3
        except FileNotFoundError:
            return emptylist
