#!/usr/bin/python3
"""100-my_int.py"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, value):
        """Override == with != """
        return self.real != value

    def __ne__(self, value):
        """Override != with == """
        return self.real == value
