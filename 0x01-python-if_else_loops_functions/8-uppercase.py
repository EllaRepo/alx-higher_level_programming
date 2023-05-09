#!/usr/bin/python3
def uppercase(str):
    for c in str:
        u = c
        if ord(c) > 96 and ord(c) < 123:
            u = chr(ord(c) - 32)
        print("{}".format(u), end='')
    print("")
