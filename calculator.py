import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

#divisha
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b



def logarithm(a, b):
    if a<=0 or b<=0 or b==1:
        raise ValueError


    return math.log(b,a)

def exponential(a, b):
    return a**b



def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b < 0 or a < 0 or b == 1:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b
