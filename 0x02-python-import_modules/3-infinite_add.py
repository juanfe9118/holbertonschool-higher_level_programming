#!/usr/bin/python3
from sys import argv
res = 0

if __name__ == "__main__":
    for i, j in enumerate(argv):
        if i != 0:
            res += int(j)
    print("{:d}".format(res))
