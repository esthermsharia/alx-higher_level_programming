#!/usr/bin/python3

"""Defines a rectangle"""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Se the width of the rectangle"""
        if value < 0:
            raise ValueError("width must be >0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if value < 0:
            raise ValueError("height must be >=0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__value = value
