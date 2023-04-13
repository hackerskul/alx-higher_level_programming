#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is negative
    if idx < 0:
        # Return a copy of the original list
        return my_list[:]
    # Check if idx is out of range
    elif idx >= len(my_list):
        # Return a copy of the original list
        return my_list[:]
    else:
        # Create a new list with the same elements as my_list
        new_list = my_list[:]
        # Replace the element at the specified index with the new element
        new_list[idx] = element
        # Return the new list with the updated element
        return new_list
