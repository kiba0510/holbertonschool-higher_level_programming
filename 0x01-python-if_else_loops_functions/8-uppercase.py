#!/usr/bin/python3
# Python function that prints a string
# in uppercase followed by a new line.
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - ord(' '))
        print('{:s}'.format(c), end='')
    print('\n', end='')
