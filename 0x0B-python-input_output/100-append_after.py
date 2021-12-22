#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line 
    containing a specific string"""
    with open(filename, "r") as f:
        contents = f.readlines()

    with open(filename, "w") as f:
        i = 0
        for j in contents:
            i += 1
            if search_string in j:
                contents.insert(i, new_string)
            f.write(j)
