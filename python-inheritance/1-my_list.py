#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    """Mylist, subclass of list

    Functions:
        print_sorted(self)

    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        print(sorted(self))
