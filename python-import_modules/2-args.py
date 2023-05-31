#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    len_argv = len(argv)
    if len_argv == 1:
        print(f"{len_argv - 1} argument.")
    elif len_argv == 2:
        print(f"{len_argv - 1} argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{len_argv - 1} arguments:")
        for i in range(1, len_argv):
            print(f"{i}: {argv[i]}")
