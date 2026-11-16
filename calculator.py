import math

def add(a, b):
    return a + b

def square_root(a):
    try:
        if a < 0:
           raise ValueError("Cannot compute the square root of a negative number.")
        return math.sqrt(a)
    except ValueError as error:
        print(str(error))

def hypotenuse(a, b):
    return math.hypot(a,b)

def subtract(a, b):
    return a-b

def logarithm(a, b):
    if a<=0 or b<=0 or b==1:
        raise ValueError


    return math.log(b,a)

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a ** b
#
