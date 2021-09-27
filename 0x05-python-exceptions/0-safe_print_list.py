#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = sum(1 for x in my_list)
        if i < x:
            print(*my_list[:], sep="")
            return i
        else:
            print(*my_list[:x], sep="")
            return x
    except:
        print("no es por aca")
