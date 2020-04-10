#!/usr/bin/python3
"""Module to find the peak in an integer list"""


def find_peak(list_of_integers):
    """Finds the peak in a list of integers"""
    if not is list_of_integers:
        return None
    if len(list_of_integers) >= 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[-1]
        return find_peak_rec(list_of_integers, 0, len(list_of_integers))
    return list_of_integers[0]


def find_peak_rec(_list, start, end):
    """Finds the peak recursively"""
    if end - start < 2:
        return None
    mid = (start + end) // 2
    if _list[mid] > _list[mid + 1] and _list[mid] > _list[mid - 1]:
        return _list[mid]
    return find_peak_rec(_list, start, mid) or find_peak_rec(_list, mid, end)
