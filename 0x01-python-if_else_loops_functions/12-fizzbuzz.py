#!/usr/bin/python3


def fizzbuzz():
    for n in range(1, 101):
        if n % 5 == 0 and n % 3 == 0:
            print("Fizzbuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(n), end=" ")
