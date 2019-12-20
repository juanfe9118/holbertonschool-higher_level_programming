#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    new = list(sorted(a_dictionary))
    for i in range(len(new)):
        print("{:s}: {}". format(new[i], a_dictionary[new[i]]))
