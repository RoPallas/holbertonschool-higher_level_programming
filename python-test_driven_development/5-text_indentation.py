#!/usr/bin/python3
"""Define a function that modify and print a text"""


def text_indentation(text):
    """The function prints a text
    with 2 new lines after each of these characters:
    ., ? and :

    Arguments:
        text (str): The text to modify and print
    Raises:
        TypeError: if text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    new_text = ""

    for ch in text:
        new_text += ch
        if ch in chars:
            new_text += "\n\n"

    lines = new_text.splitlines()
    text_to_print = []

    for line in lines:
        new_line = line.strip()
        text_to_print.append(new_line)

    print("\n".join(text_to_print), end="")
