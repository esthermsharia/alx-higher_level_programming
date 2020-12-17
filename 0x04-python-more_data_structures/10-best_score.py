#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    val = list(a_dictionary.keys())[0]
    biggest = a_dictionary[val]
    for i, j in a_dictionary.items():
        if j > biggest:
            biggest = j
            val = i
    return (val)
