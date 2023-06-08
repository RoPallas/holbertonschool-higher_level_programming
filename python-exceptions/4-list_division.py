#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            d = my_list_1[i] if i < len(my_list_1) else 0
            r = my_list_2[i] if i < len(my_list_2) else 0
            if not isinstance(d, (int, float)):
                raise TypeError("wrong type")
            elif not isinstance(r, (int, float)):
                raise TypeError("wrong type")
            if r == 0:
                raise ZeroDivisionError("division by 0")
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            result = d / r
            results.append(result)
        except ZeroDivisionError:
            print("division by 0")
            results.append(0)
        except TypeError as e:
            print(e)
            results.append(0)
        except IndexError:
            print("out of range")
            results.append(0)
        finally:
            pass
    return results
