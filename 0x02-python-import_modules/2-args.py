#!/usr/bin/python3
import sys
if __name__ == '__main__':
    nargs = len(sys.argv)
    if nargs == 1:
        print("0 arguments.")
    else:
        print("{} arguments.".format(nargs-1))
        for item in sys.argv[1:]:
            print("{} : {}".format(sys.argv.index(item), item))
