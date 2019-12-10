#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i >= j:
            continue
        if i != 8 or j != 9:
            print ("{:d}{:d}, " .format(i, j), end="")
        if i == 8 and j == 9:
            print("{:d}{:d}" .format(i, j))
