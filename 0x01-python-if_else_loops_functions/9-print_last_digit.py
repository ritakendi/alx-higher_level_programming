#!/usr/bin/python3
def print_last_digit(number):
    i = 0
    if number < 0:
        number *= -1
        i = 1
        last = number % 10
        if i == 1:
            number *= -1

    print("{:d}".format(last), end='')
    return (last)
