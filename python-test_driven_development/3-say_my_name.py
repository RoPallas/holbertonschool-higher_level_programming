#!/usr/bin/python3
"""Define a function to say a name"""


def say_my_name(first_name, last_name=""):
    """The function prints My name is <first name> <last name>

    Args:
        first_name (str): The first name
        last_name (str): The last name
    Raises:
        TypeError: when any of the args is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
