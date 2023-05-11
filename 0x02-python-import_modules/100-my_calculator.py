#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = sys.argv[2]
    c = int(sys.argv[3])
    if b == '+':
        print("{} {} {} = {}".format(a, b, c, add(a, c)))
    elif b == '-':
        print("{} {} {} = {}".format(a, b, c, sub(a, c)))
    elif b == '*':
        print("{} {} {} = {}".format(a, b, c, mul(a, c)))
    elif b == '/':
        print("{} {} {} = {}".format(a, b, c, div(a, c)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
