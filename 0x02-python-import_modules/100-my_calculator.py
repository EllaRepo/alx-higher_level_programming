#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = ['+', '-', '*', '/']
    a = int(sys.argv[1])
    b = sys.argv[2]
    c = int(sys.argv[3])
    index = op.index(b)
    if index == 0:
        print("{} {} {} = {}".format(a, b, c, add(a, c)))
    elif index == 1:
        print("{} {} {} = {}".format(a, b, c, sub(a, c)))
    elif index == 2:
        print("{} {} {} = {}".format(a, b, c, mul(a, c)))
    elif index == 3:
        print("{} {} {} = {}".format(a, b, c, div(a, c)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
