#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary)
    new_dic = dict()
    for ids in keys:
        new_dic[ids] = a_dictionary[ids] * 2
    return new_dic
