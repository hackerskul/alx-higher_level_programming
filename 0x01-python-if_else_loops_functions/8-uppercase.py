#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - ord('a') + ord('A')), end="")
        else:
            print("{}".format(char), end="")
