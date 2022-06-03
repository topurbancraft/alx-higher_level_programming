#!/usr/bin/python3
def no_c(my_string):
    '''
    Prints the items in a list of integers except characters 'c' or 'C'
    Parameters:
    my_list (list): The list of integers
    '''
    new = ""
    i = 0
    while i < len(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            i += 1
            continue
        new += my_string[i]
        i += 1
    return new
