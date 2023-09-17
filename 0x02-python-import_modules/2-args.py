#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    argvlength = len(sys.argv) - 1

    if (argvlength == 0):
        print("0 arguments.")
    elif (argvlength == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(argvlength))
        number = 1
        for argument in range(argvlength):
            print("{}: {}".format(number, argument))
            number += 1
