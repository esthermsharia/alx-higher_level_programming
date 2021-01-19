#!/usr/bin/python3

"""module defines a class Student."""


class Student:
    """class represents a student."""

    def __init__(self, first_name, last_name, age):
        """initializes a new student..
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return  dictionary representation of a Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
