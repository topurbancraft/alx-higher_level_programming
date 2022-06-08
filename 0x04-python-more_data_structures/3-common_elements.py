#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''
    Returns common items in both sets
    Parameters:
    set_1, set_2: The sets that would be compared
    '''
    set_com = set_1 & set_2
    return set_com
