#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    key = list(new.keys())
    for i in range(len(key)):
        new[key[i]] = new[key[i]] * 2
    return new
