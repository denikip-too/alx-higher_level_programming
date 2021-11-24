#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = dict(a_dictionary)
    for key, value in dictionary.items():
        dictionary[key] = value * 2
    return dictionary
