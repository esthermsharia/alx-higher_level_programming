#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in my_list:
        if i % 2:
            bool_list = bool_list + [False]
        else:
            bool_list = bool_list + [True]
    return bool_list
