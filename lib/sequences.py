#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    if length == 1: 
        my_list.append(0)
    elif length == 2: 
        my_list.append(0)
        my_list.append(1)
    elif length > 2: 
        my_list.append(0)
        my_list.append(1)
        for i in range(2, length): 
            my_list.append(my_list[i - 1] + my_list[i - 2])
    else: 
        pass
    print(my_list)