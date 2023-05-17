#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    for id in keys:
        print("{}: {}".format(id, a_dictionary.get(id)))
