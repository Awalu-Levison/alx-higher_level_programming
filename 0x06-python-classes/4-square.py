#!/usr/bin/python3
""" defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """defining the public method
        method:
            area():
                return area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter method
        used to access private instance
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Set new value to the
        Args:
            size:
                privatye instance variable
        """
        self.__size = size
