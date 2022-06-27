#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) in [int, float]:
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) in [int,float]:
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    result = a + b
    return result
