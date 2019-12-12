#!/usr/bin/python3
import hidden_4

array = dir(hidden_4)
for i in array:
    if i[:2] != '__':
        print(i)
