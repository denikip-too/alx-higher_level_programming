#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """prints the list in sorted order"""

    def print_sorted(self):
        print(sorted(self))
