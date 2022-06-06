#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for left in range(len(matrix)):
        for right in range(len(matrix[left])):
            if right != 0:
                print(" ", end='')
            print("{:d}".format(matrix[left][right]), end='')
        print()
