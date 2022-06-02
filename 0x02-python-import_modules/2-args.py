#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
if len(arguments) == 1:
    print(f"{len(arguments)} argument:")
elif len(arguments) == 0:
    print(f"{len(arguments)} argument.")
else:
    print(f"{len(arguments)} arguments:")
for index, arg in enumerate(arguments,):
    print(f"{index + 1}: {arg}")

# for i in range (len(a)):
#     print("{}+ {} + {}.format(arg, :, /n")
#     return(len(*args))
