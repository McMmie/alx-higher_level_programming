#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char = ord(char)
        if (char >= 97) & (char <= 122):
            char = char - 32
        char = chr(char)
        print(f"{char}", end='')
    print(f"")
