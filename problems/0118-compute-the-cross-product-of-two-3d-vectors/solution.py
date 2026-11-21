import numpy as np

def cross_product(a, b):
    cross = [None, None, None]
    cross[0] = a[1]* b[2] - a[2]*b[1]
    cross[1] = -a[0] * b[2] + a[2]*b[0]
    cross[2] = a[0]*b[1] - a[1]*b[0]
    return cross
    pass