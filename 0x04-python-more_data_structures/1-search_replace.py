#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new = my_list[:]
    for i in range(my_list.count(search)):
        j = new.index(search)
        new[j] = replace
    return new

