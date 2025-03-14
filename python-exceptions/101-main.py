#!/usr/bin/python3
# Import the safe_function from the file
safe_function = __import__('101-safe_function').safe_function

# Function 1: my_div - A simple division function
def my_div(a, b):
    return a / b

# Test 1: Safe execution of my_div
result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

# Test 2: Division by zero (Error case)
result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))

# Function 2: print_list - A simple function that prints elements from a list
def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

# Test 3: Safe execution of print_list
result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
