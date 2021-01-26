#!/usr/bin/python3
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter method for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle with the character #"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)


    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if args is not None:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "x" in kwargs:
                self.x = kwargs["x"]
