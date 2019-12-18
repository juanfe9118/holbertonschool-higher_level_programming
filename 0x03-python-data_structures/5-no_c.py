#!/usr/bin/python3


def no_c(my_string):
    my_list = []
    for i in range(len(my_string)):
        my_list.append(my_string[i])
    for i in range(my_list.count('c')):
        my_list.remove('c')
    for i in range(my_list.count('C')):
        my_list.remove('C')
    new_string = ""
    for i in range(len(my_list)):
        new_string = new_string + my_list[i]
    return new_string
