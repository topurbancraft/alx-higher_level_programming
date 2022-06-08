#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''
    Returns items that are unique to both set
    Parameters:
    set_1, set_2: The sets that would be compared
    '''
    dif_item = set_1 ^ set_2
    return dif_item
