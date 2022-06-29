#!/usr/bin/python3
'''
A module for working with rectangles.
'''


class Rectangle:
    '''
    Represents a 2D 4 sided Polygon with 2 set of equal sides..
    '''
    def __init__(self, width=0, height=0):
        '''Initializes a Rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The position of the rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieves the width of this Rectangle.
        Returns:
            int: The width of this Rectangle.
        '''
        return self.__width

    @property
    def height(self):
        '''Retrieves the height of this Rectangle.
        Returns:
            int: The height of this Rectangle.
        '''
        return self.__height

    @width.setter
    def width(self, value):
        '''Updates the width of this Rectangle.
        Args:
            value (int): The new width of this Rectangle.
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        else:
            if value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value

    @height.setter
    def height(self, value):
        '''Updates the height of this Rectangle.
        Args:
            value (int): The new height of this Rectangle.
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        else:
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
