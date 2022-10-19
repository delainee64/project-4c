# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/18/2022
# Description: Write a function named hailstone that takes a positive integer parameter as
# the initial number of a hailstone sequence and returns how many steps it takes to reach 1.

def hailstone(pos_int):
    """function takes a positive integer parameter as the initial number of a
    hailstone sequence and returns how many steps it takes to reach 1."""
    steps = 0  # steps to zero
    while pos_int != 1:
        if pos_int % 2 == 0:  # when the integer is positive.
            pos_int //= 2
        else:
            pos_int = 3 * pos_int + 1
        steps += 1  # increases the steps by 1
    return steps  # returns number of steps taken


# print(hailstone(1))
# print(hailstone(3))
# print(hailstone(1000))
