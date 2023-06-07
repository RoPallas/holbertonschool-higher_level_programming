#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n_e = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            n_e += 1
    except IndexError:
        pass
    finally:
        print()
        return n_e
