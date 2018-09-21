#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    death_list = []
    for k, v in a_dictionary.items():
        if v == value:
            death_list.append(k)
    for k in death_list:
        del a_dictionary[k]
    return (a_dictionary)
