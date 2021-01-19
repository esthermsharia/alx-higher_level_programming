#!/usr/bin/python3

"""Module defines a fxn that appends a string to the end of a text file.."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 encoded file.
    Args:
        filename (str): Name of file to append to.
        text (str): String to append to filename.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
