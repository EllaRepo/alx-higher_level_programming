#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    _key = ""
    score = 0
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            _key = key
    return _key if _key in a_dictionary else None
