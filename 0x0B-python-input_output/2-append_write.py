#!/usr/bin/python3
"""defines a file append function"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file
    Args:
        filename(str): name of the text file
        text(str): text to be written
    Return: number of characters added.
    """
    with open(filename, "a", encoding="UTF-8")as f:
        return f.write(text)
