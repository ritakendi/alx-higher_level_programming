#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for elements in range(x):
    
        try:
            print("{}".format(my_list[elements]), end="")
        except IndexError:
            break
        
safe_print_list([1, 2, 3, 4], 2)