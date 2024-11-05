#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        cpy = a_dictionary.copy()
        a_list = []
        for key in cpy:
            a_list.append(cpy[key])
        top = a_list[0]
        for i in a_list:
            if i > top:
                top = i
        for keys in a_dictionary:
            if a_dictionary[keys] == top:
                return keys
