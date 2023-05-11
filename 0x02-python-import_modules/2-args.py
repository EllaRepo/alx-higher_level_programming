#!/usr/bin/python3
import sys
if __name__ == '__main__':
    nargs = len(sys.argv) - 1
    msg_end = "s." if nargs == 0 else (":" if nargs == 1 else "s:")
    print("{} argument{}".format(nargs, msg_end))
    for item in sys.argv[1:]:
        print("{}: {}".format(sys.argv.index(item), item))
