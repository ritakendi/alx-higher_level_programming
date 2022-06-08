#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bst_score = -1
    best_key = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > bst_score:
            bst_score = a_dictionary[key]
            best_key = key
    return best_key
