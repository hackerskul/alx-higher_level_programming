#!/usr/bin/python3
def best_score(a_dictionary):
    b = 0
    for k, v in a_dictionary.items():
        if v > b:
            b = v
        else:
            return None
    return b
