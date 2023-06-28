#!/usr/bin/python3
"""
This module creates a class Square.
"""


class Square:
    """
    A class named Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new private instance of the Square class.
        And raises TypeError and ValueError

        Args:
            size (int): Size of square.
            position (tupil): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter of size for the class Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size for the class Square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter of position for the class Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of position for the class Square
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not isinstance(value[0], int) \
                or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates area of square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print("#", end='')
            print()

    def __str__(self):
        s = ''
        if self.__size == 0:
            return ''
        for i in range(self.__position[1]):
            s += '\n'
        for i in range(self.__size):
            for k in range(self.__position[0]):
                s += ' '
            for j in range(self.__size):
                s += '#'
            if i != self.__size - 1:
                s += '\n'
        return s
