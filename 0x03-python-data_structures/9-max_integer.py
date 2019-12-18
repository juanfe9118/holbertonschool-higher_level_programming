#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = len(my_list) - 1
    my_list.sort()
    return my_list[i]
