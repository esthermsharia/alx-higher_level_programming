#!/usr/bin/python3
def no_c(my_string):
    str_modified = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            str_modified += char
    return str_modified
