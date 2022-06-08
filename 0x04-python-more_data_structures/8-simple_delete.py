#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''
    Returns keys or values of keys in a dictionary
    Parameters:
    a_dictionary: Dictionary with keys
    '''
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
