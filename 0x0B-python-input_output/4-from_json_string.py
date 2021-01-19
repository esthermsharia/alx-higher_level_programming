#!/usr/bin/python3

"""Module defines a fxn that returns object representation by a JSON string."""
import json


def from_json_string(my_str):
    """Return python object representation of a JSON string."""
    return json.loads(my_str)
