#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [printf("{}: {}".format(k, a_dictionary)) for k in sorted(a_dictionary)]
