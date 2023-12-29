#!/usr/bin/python3
import sys


def print_arguments():
    nmbr = len(sys.argv) - 1

    if nmbr == 0:
        print("arguments")
    elif nmbr == 1:
        print("1 argument:")
    else:
        print(nmbr, "arguments:")

    for i in range(1, len(sys.argv)):
        print(f"{i}:", sys.argv[i])


print_arguments()
