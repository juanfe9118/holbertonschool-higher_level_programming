#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    lis = my_list.reverse()
    for i in range(len(lis)):
        print("{:d}".format(lis[i]))
