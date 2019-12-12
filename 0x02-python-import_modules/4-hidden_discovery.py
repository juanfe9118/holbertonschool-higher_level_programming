#!/usr/bin/python3
import hidden_4

array = dir(hidden_4)
if __name__ == "__main__":
    for i in array:
        if i[:2] != '__':
            print(i)
