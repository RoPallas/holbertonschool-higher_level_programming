#!/usr/bin/python3
"""Function read_file"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout"""

    with open(filename, encoding="UTF8") as file:
        text = file.read()
        print(text)
