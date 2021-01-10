#!/usr/bin/python3
def add_integer(a, b):
    """
    Function that sums 2 integers
    a (int or float)
    b (int or float)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a most be an integer")
    
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    return int(a + b)
