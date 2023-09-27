#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    argvlength = len(sys.argv) - 1

    if (argvlength == 0):
        print("0 arguments.")
    elif (argvlength == 1):
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argvlength))
        number = 1
        for argument in range(argvlength):
            print("{}: {}".format(number, sys.argv[argument + 1]))
            number += 1
