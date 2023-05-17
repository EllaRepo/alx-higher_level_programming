#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num, denum = 0, 0
    for score, weight in my_list:
        num += score * weight
        denum += weight
    return num / denum
