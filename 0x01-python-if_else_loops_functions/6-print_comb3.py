#!/usr/bin/python3
n = 0
for i in range(10):
    j = 1 + n
    while j < 10:
        print("{}{}".format(i, j), end="")
        if i == 8and j == 9:
            break
        j += 1
        print(",", end=" ")
    n += 1
print("")
