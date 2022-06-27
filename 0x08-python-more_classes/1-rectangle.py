#!/usr/bin/python3
"""Rectangle class
A class that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle

    Attributes:
    __width: width of the rectangle
    __height: height of the rectangle

    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle

        Args:
            width (int): width of rect
            height (int): height of rect

            Returns:
                None
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter of __width
        Returns:
            The width of the rect
            """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width

        Returns:
            None
        """
        if type(value) in [int]:
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """getter of __height

        Returns:
            The width of the rect
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Returns:
            None
        """
        if type(value) in [int]:
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')
