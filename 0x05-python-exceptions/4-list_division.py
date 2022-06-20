#!/usr/bin/python3
from cgitb import reset
from decimal import DivisionByZero


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for elements in range(list_length):
        try:
            result = my_list_1[elements] / my_list_2[elements]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list