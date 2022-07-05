#!/usr/bin/python3
"""defines a text file  write function"""


def write_file(filename="", text=""):
    """writes a string to a text file.
    Args:
        filename (str): name of file.
        text (str): text to be written.
    Return: the number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8")as f:
        return(f.write(text))
