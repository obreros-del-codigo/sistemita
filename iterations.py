from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from plot import plotting


def foo_dynamic(formulae_str,a0,b0,n0,x0,it):
    x,a,b,n=symbols("x a b n")
    y = sympify(formulae_str)
    y = y.subs(a,a0)
    y = y.subs(b,b0)
    y = y.subs(n,n0)
    print(y)

    f=lambdify(x,y,"numpy")

    z = x0

    y1 = []

    for i in range(it):
        z = f(z)
        y1.append(z)

    return y1

def foo_iterations(formulae_str,A,B,N,X0, it):
    fig, ax = plt.subplots()
    for a in A:
        for b in B:
            for n in N:
                for x in X0:
                    y1=foo_dynamic(formulae_str,a,b,n,x,it)
                    filename=formulae_str+"_a"+str(a)+"_b"+str(b)+"_n"+str(it)+"_x0"+str(x)+"_i"+str(n)+".png"
                    caption = "a="+str(a)+" b="+str(b)+" n="+str(n)+" x0="+str(x)+" i="+str(it)
                    plotting(fig, ax, y1,formulae_str,filename,caption)


