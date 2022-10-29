#!/usr/bin/python3
"""
direct or indirect class inheritance
"""


def inherits_from(obj, a_class):
    """returns true when obj is subclass of a_class or otherwise"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
