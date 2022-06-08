#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''
    Returns the value of keys multiplied by 2
    Parameters:
    a_dictionary: Dictionary with keys
    '''
    return {key: val*2 for key, val in a_dictionary.items()}
