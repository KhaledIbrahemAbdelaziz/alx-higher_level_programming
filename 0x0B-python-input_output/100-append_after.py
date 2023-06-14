#!/usr/bin/python3
"""Define the append after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string"""
    text = ""
    with open(filename) as f:
        for l in f:
            text += l
            if search_string in l:
                text += new_string
    with open(filename, "w") as wr:
        wr.write(text)
