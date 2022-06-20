#!/usr/bin/python3
#value can be any type.
#Return True if value is an integer
#Return False otherwise
def safe_print_integer(value):
    try:
        print("{.d}".format(value))
    except:
        return (False)
    else:
        return (True)
