#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while my_list[i] and i < x:
            print("{}".format(my_list[i]), end='')
            i += 1
    except IndexError:
        pass
    print()
    return i
