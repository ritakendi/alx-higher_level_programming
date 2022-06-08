#!/usr/bin/python3
<<<<<<< HEAD
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
=======
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    w = 0
    we = 0
    for t in my_list:
        w += t[1]
        we += t[0] * t[1]
    return we / w
>>>>>>> fcfa246523b3c1ba20579a9dc7feee6f6d9b174a
