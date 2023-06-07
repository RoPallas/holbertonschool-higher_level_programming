#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers = []
    r = 0
    for i in my_list:
        if i not in numbers:
            numbers.append(i)
            r += i
    return r
