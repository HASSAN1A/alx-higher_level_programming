#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    bigger = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > bigger:
            bigger = my_list[i]

    return (bigger)
