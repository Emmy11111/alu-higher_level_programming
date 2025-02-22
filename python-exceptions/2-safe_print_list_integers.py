#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            print("Traceback (most recent call last):")
            print("  File \"<stdin>\", line 1, in <module>")
            print("IndexError: list index out of range")
            break
        except (ValueError, TypeError):
            pass
    print()  # Print a newline after printing the integers
    return count

