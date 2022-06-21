# #!/usr/bin/python3
# Square = __import__('0-square').Square

# my_square = Square()
# print(type(my_square))
# print(my_square.__dict__)

#!/usr/bin/python3
# Square = __import__('1-square').Square

# my_square = Square(3)
# print(type(my_square))
# print(my_square.__dict__)

# try:
#     print(my_square.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square.__size)
# except Exception as e:
# #     print(e)

# #!/usr/bin/python3
# Square = __import__('2-square').Square

# my_square_1 = Square(3)
# print(type(my_square_1))
# print(my_square_1.__dict__)

# my_square_2 = Square()
# print(type(my_square_2))
# print(my_square_2.__dict__)

# try:
#     print(my_square_1.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square_1.__size)
# except Exception as e:
#     print(e)

# try:
#     my_square_3 = Square("3")
#     print(type(my_square_3))
#     print(my_square_3.__dict__)
# except Exception as e:
#     print(e)

# try:
#     my_square_4 = Square(-89)
#     print(type(my_square_4))
#     print(my_square_4.__dict__)
# except Exception as e:
#     print(e)



#     #!/usr/bin/python3
# """MagicClass module.

# This module contains the MagicClass class used for the bytecode exercise.
# """


# import math


# class MagicClass():
#     """Defines a MagicClass object."""

#     def __init__(self, radius=0):
#         """Sets the necessary attributes for the MagicClass object.

#         Args:
#             radius (int, float): the radius of the circle
#         """
#         self.__radius = 0
#         if type(radius) is not int and type(radius) is not float:
#             raise TypeError("radius must be a number")
#         self.__radius = radius

#     def area(self):
#         """Returns the current circle area."""
#         return self.__radius ** 2 * math.pi

#     def circumference(self):
#         """Returns the current circle circumference."""
#         return 2 * math.pi * self.__radius