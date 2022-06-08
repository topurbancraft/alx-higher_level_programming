#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    Returns the addition of unique numbers in a list.
    Parameters:
    my_list (list): The list of integers
    '''
    my_list = set(my_list)
    add_num = 0
    for i in my_list:
        add_num += i
    return add_num
