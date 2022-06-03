#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''
    Prints the items in a list of integer lists
    Parameters:
    matrix (list): The list of integer lists
    '''
    for row in matrix:
        for col in range(len(row)):
            print('{:d}'.format(row[col]), end=(' ' * (col < len(row) - 1)))
        print('')
