#!/usr/bin/python3
def uppercase(str):
    for i in str:
        change = 0
        if ord(i) > 96 and ord(i) < 123:
            change = 32
        print("{:s}".format(chr(ord(i) - change)), end="")
    print()
