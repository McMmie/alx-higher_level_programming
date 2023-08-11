#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if j == i:
            continue
        elif j > i:
            if (i == 8) & (j == 9):
                print(f"{i}{j}")
            else:
                print(f"{i}{j}", end=', ')
