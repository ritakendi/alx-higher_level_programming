#!/usr/bin/python3
"""class square that defines a square"""


class Square:

    def __init__(self, size=0):
        """size must be an integer"""

        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")