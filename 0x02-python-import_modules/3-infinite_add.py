#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    i = 1
    sum = 0
    while i <= len(argv):
        sum += int(sys.argv[i])
        i += 1
    print("{}".format(sum))
