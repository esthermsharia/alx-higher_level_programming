#!usr/bin/python3
"""
This module defines the rectangle class

"""

from models.base import Base


class Rectangle(Base):
    """Class denotes a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle properties"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for the width"""
        return self.__width

    @property
    def height(self):
        """getter method for the height"""
        return self.__height

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @height.setter
    def height(self, value):
        """setter method for height"""
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter method for the width"""
        self.__width = value

    @y.setter
    def y(self, value):
        """Setter method for y"""
        self.__y = value

    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.__x = value
