#!/usr/bin/python3
"""Function write_file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written"""

    with open(filename, "w", encoding="UTF8") as file:
        n = file.write(text)
        return n
