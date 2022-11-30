#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        if ord(i) >= 97 and ord(i) <= 122:
            x = ord(i) - 32
            y = chr(x)
        else:
            y = 1
        print("{}".format(y), end="")
    print()
