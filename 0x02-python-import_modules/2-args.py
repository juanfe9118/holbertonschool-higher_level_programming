#!/usr/bin/python3
from sys import argv
arlen = len(argv) - 1
arstr = ""
if arlen == 1:
    arstr = "argument"
else:
    arstr = "arguments"
if __name__ == "__main__":
    if arlen == 0:
        print("{:d} {:s}.".format(arlen, arstr))
    else:
        print("{:d} {:s}:".format(arlen, arstr))
        for i, j in enumerate(argv):
            if i != 0:
                print("{:d}: {:s}".format(i, j))
