#!/usr/bin/python3
"""Function that checks if an object is
    exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """true if an object is same class as a_class returns false otherwise"""
    return (type(obj) == a_class)
