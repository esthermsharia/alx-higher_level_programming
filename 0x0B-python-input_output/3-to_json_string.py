#!/usr/bin/python3

"""Module defines a fxn that returns a json representation of an object."""
import json


def to_json_string(my_obj):
    """ReturnJSON representation of a string object."""
    return json.dumps(my_obj)
