#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    i = 1
    if len(argv) == 0:
        print("{} arguments.".format(0))
    elif len(argv) == 1:
        print("{} argument:".format(len(argv)))
        print("{}: {}".format(len(argv), str(sys.argv[1])))
    else:
        print("{} arguments:".format(len(argv)))
        while i <= len(argv):
            print("{}: {}".format(i, str(sys.argv[i])))
            i += 1
