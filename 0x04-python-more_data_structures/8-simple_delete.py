#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
    except:
        return a_dictionary 
    return a_dictionary
