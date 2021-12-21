#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes a string and returns the number of characters written to a file"""
    with open(filename, mode="w", encoding="utf-8") as Myfile:
        return Myfile.write(text)
