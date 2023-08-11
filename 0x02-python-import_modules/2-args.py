#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    _len = (len(argv)) - 1
    i = 1
    if _len == 0:
        print(f"0 arguments.")
    elif _len == 1:
        print(f"1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{_len} arguments:")
        for arg in argv:
            if arg == argv[0]:
                continue
            else:
                print(f"{i}: {arg}")
                i += 1
