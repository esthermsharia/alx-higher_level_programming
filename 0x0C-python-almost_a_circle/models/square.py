#!/usr/bin/python3
"""
This module defines the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter method  for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)
