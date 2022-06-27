#!/usr/bin/python3
"""Rectangle class
A class that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """calculates the area of rectangle
        Return:
            Area of a rectangle
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """calculates the area of a rectangle
        Return:
            Area of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return((self.width + self.height) * 2)

    @property
    def width(self):
        """getter of __width

        Return:
            width of the rectangle
        """
        return self.width

    @width.setter
    def width(self, value):
        """__width setter
        Return:
            None
        """
        if type(value) in [int]:
            if value < 0:
                raise ValueError('width must be >= 0')
            self.width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """getter of __height

        Returns:
            The height of the rect
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