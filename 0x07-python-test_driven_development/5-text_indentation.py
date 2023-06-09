#!/usr/bin/python3
""" This module defines a function that prints a text with 2 new
    lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new
    lines after each of these characters: ., ? and

    Args:
        text: a text
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    txt = text[:]
    for delim in '.:?':
        txt_list = txt.split(delim)
        txt = ""
        for i in txt_list:
            i = i.strip(" ")
            txt = i + delim if txt is "" else txt + "\n\n" + i + delim
    print(txt[:-3], end="")
