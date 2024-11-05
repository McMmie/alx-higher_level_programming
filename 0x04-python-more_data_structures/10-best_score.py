#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    lst = []
    for keys, value in a_dictionary.items():
        lst.append(value)
    return list(filter(lambda x: a_dictionary[x] == max(lst), a_dictionary))[0]
