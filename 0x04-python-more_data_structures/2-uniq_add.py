#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        tmp = my_list.copy()
        for i in range(len(my_list)):
            for j in range(i + 1, len(my_list)):
                if tmp[j] == tmp[i]:
                    tmp[j] = 0
        sum = 0
        for i in tmp:
            sum += i
        return (sum)
