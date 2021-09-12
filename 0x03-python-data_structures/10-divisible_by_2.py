#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiplos = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiplos.append(True)
        else:
            multiplos.append(False)

    return (multiplos)
