#!/usr/bin/python3
def magic_calculation(a, b):
    c = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                c += a ** b / i
        except:
            c = a + b
    return c
