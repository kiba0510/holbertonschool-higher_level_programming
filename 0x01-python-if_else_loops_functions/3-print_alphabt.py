#!/usr/bin/python3
# lowercase printing ommiting 'e' and 'q'
for i in range(ord('a'), ord('z') + 1):
    if (i != 101 and i != 113):
        print("{}".format(chr(i)), end="")
