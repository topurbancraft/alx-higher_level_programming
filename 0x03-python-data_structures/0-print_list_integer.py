#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''
    Prints the items in a list of integers
    Parameters:
    my_list (list): The list of integers
    '''
    i = 0
    while i < len(my_list):
        print("{:d}".format(my_list[i]))
        i += 1
