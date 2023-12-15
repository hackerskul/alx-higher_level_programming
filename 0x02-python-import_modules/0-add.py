#!/usr/bin/python3
from 0-add import add
# Define a and b on separate lines
a = 1
b = 2

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))
