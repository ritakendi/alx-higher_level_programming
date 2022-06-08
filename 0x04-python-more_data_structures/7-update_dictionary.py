#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return 0
    a_dictionary[key] = value
    return a_dictionary
