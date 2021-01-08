#!/usr/bin/python3

"""Integer addition function.
   Performs addition of 2 values
   only floats and integers are accepted.
   with the 2nd argument b defaulting to 98
"""


def add_integer(a, b=98):
    """Add a to b and return the result.
    All arguments that are floats will be typecasted to ints
    Raises:
        TypeError: when a or b are neither integers nor floats.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
