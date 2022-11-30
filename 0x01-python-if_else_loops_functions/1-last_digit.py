#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of "
lastnum = number % 10
if number < 0:
    lastnum = (-1 * number) % 10
    lastnum = -lastnum
if lastnum > 5:
    print("{}{} is {} and is greater than 5".format(str1, number, lastnum))
elif lastnum == 0:
    print("{}{} is {} and is 0".format(str1, number, lastnum))
else:
    print("{}{} is {} and is less than 6 and not 0"
          .format(str1, number, lastnum))
