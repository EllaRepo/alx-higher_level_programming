#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, j = 0, 0
    while i < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                j += 1
        except IndexError:
            raise
        i += 1
    print()
    return j
