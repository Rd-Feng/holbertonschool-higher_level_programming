#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return sorted(a_dictionary.items(),
                      key=lambda e: e[1], reverse=True)[0][0]
