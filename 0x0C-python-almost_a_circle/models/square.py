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

    def update(self, *args, **kwargs):
        """update attributes"""
        if (args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "size" in kwargs:
                self.size = kwargs["size"]

    def to_dictionary(self):
        """dictionary representation of a Square"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["y"] = self.y
        dictionary["x"] = self.x
        return dictionary
