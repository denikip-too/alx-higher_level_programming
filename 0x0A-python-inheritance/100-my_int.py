#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """Inherits from int
    """

    def __eq__(self, value):
        """Magic method with operator equals"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Magic method with operator not equals"""
        return super().__eq__(value)
