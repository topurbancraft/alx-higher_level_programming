#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''
    Returns the keys in a dictionary in alphabetical order
    Parameters:
    a_dictionary: Dictionary with keys
    '''
    for m in sorted(a_dictionary.keys()):
        print("{}: {}".format(m, a_dictionary[m]))
