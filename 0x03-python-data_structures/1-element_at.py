#!/usr/bin/python
def element_at(my_list, idx):
    if idx < 0:
        return "None"
    if idx > len(my_list):
        return "None"
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
