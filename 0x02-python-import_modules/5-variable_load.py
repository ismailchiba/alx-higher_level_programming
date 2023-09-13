#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Len = len(sys.argv)
    if Len == 1:
        print("{} arguments.".format(Len - 1))
    elif Len == 2:
        print("{} argument:".format(Len - 1))
    else:
        print("{} arguments:".format(Len - 1))
    for i in range(1, Len):
        print("{}: {}".format(i, sys.argv[i]))
