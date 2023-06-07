#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    n_roman = {"M": 1000, "D": 500, "C": 100,
               "L": 50, "X": 10, "V": 5, "I": 1}
    result = 0
    v_prev = 1000
    for c in roman_string:
        v = n_roman.get(c, 0)
        if v == 0:
            return 0
        if v <= v_prev:
            result += v
        else:
            result += v - v_prev * 2
        v_prev = v
    return result
