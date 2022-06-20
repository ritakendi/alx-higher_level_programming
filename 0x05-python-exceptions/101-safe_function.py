#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    """Returns the result of the function,
    Otherwise,
    returns None if something happens during the function
    and prints in stderr the error precede by Exception:"""
    try:
        result = fct(*args)

    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None

    return result