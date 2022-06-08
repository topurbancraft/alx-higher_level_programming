#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    Prints the items in a list of integers
    Parameters:
    my_list (list): The list of integers
    '''
    c = len(matrix[0])
    new_matrix = [[(m[i] ** 2) for i in range(c)] for m in matrix]
    return new_matrix
