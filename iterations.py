from sympy import *
import numpy as np

from sympy import *

def foo_iterations(a,b,x0,i,n,formulae_str):
    inicial= x0
    x = Symbol("x")
    y=sympify(formulae_str)
    yprime=y.diff(x)
    f=lambdify(x,y,"numpy")

    rangei=range(7)

    xl=[]
    for i in rangei:
        inicial = f(inicial)
        xl.append(inicial)
    return xl
