#!/usr/bin/python3
"""Function load_from_json_file"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""

    import json

    with open(filename, "r", encoding="UTF8") as file:
        return json.load(file)
