#!/usr/bin/python3
# lowercase printing ommiting 'e' and 'q'
for c in range(97, 123):
    if c == 101 or c == 113:
        continue
    print(chr(c), end="")
