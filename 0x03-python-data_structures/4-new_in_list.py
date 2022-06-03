#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''
    Prints the items in a list of integers after
    an element from the list is replaced.
    Parameters:
    my_list (list): The list of integers
    idx: positioning number to identify specific list item.
    element: integer that would replace the old
    integer in a chosen position on the list.
    '''
    new_list = my_list[:]
    if idx < 0:
        return my_list
    elif (idx > (len(my_list) - 1)):
        return my_list
    else:
        new_list[idx] = element
        return new_list
