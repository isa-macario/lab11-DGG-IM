import math
#divisha
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if a== 0:
        raise ZeroDivisionError
    return b/a


def logarithmic(a, b):
    if a<=0 or b<=0 or b==1:
        raise ValueError


    return math.log(b,a)

def exponential(a, b):
    return a**b



