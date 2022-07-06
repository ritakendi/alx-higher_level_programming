#!/usr/bin/python3
"""
Has BaseGeometry and a subclass
"""


class Rectangle(BaseGeometry):
    """this is a rectangle"""
    def __init__(self, width, height):
        """instantiation of rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height