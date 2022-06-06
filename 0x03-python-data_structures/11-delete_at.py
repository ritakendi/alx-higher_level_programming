#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
<<<<<<< HEAD
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
=======
    length = len(my_list)

    if idx < 0 or idx >= length:
        return (my_list)
    else:
        del my_list[idx]

        return (my_list)
>>>>>>> 87bcb702dbec23452b06c7bba837e636e11508ae
