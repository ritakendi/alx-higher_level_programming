#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]
    if len(arguments) == 1:
        print(f"{len(arguments)} argument:")
    elif len(arguments) == 0:
        print(f"{len(arguments)} arguments.")
    else:
        print(f"{len(arguments)} arguments:")
    for index, arg in enumerate(arguments,):
        print(f"{index + 1}: {arg}")
