#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''
    Returns keys or values of keys in a dictionary
    Parameters:
    a_dictionary: Dictionary with keys
    '''
    new_dict = a_dictionary
    new_dict[key] = value
    return new_dict
