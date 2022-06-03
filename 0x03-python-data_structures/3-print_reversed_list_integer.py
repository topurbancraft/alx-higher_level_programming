#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    Prints the items in a list of integers in reverse.
    Parameters:
    my_list (list): The list of integers
    '''
    if not my_list:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
