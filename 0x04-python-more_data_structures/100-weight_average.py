#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_s, sum_w = 0, 0
    if my_list is not None and len(my_list):
        for s, w in my_list:
            sum_s += s * w
            sum_w += w
        return (sum_s / sum_w)
    return (0)
