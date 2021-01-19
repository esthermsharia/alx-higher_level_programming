#!/usr/bin/python3

"""Module defines a fxn that converts class to JSON."""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure."""
    return obj.__dict__
