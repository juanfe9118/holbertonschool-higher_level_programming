#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    try:
        key = list(a_dictionary.keys())
    except:
        return None
    score = key[0]
    for i in range(len(key)):
        if a_dictionary[score] >= a_dictionary[key[i]]:
            continue
        else:
            score = key[i]
    return score
