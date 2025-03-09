#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Call the function `fct` with arguments `*args`
        return fct(*args)
    except Exception as e:
        # If any exception occurs, print the error to stderr and return None
        print(f"Exception: {e}", file=sys.stderr)
        return None
