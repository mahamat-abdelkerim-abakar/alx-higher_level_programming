#!/usr/bin/python3
def print_last_digit(number):
    """Returns the last digit of a number."""
    if number < 0:
        ldigit = number % 10
        print("{:d}".format(ldigit), end="")
        return ldigit
