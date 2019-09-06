from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from plot import plotting
import random as rn

def foo_evaluator(formulae_str,a0,b0,n0,x0,it,d,k):
    
    x,a,b,n=symbols("x a b n")
    y = sympify(formulae_str)
    y = y.subs(a,a0)
    y = y.subs(b,b0)
    y = y.subs(n,n0)
    print(y)

    f=lambdify(x,y,"numpy")

    z = x0

    y1 = []
    if d==1:
        for i in range(it):
            z = f(z)
            y1.append(z)
    else:
        for i in x0:
            y1.append(f(i))
    for i,v in enumerate(y1):
        y1[i]=v+(rn.random()-0.5)*2.0*k
    return y1


def plot_hist (f,g,figh,axh,bind):
    data_histo=[]
    for i,(v1,v2) in enumerate(zip(f,g)):
        data_histo.append(v1-v2)
    plt.hist(data_histo, bind)
    plt.show()
    
def plot_observation(fig,ax,data):
    plt.errorbar(data)

def foo_iterations(formulae_str,A,B,N,X0, it,dynamic,k,bind,histo,obs_flag):

    fig, ax = plt.subplots()
    if histo:
        figh,axh=plt.subplots()
    for a in A:
        for b in B:
            for n in N:
                if dynamic:
                    for x in X0:
                        y1=foo_evaluator(formulae_str,a,b,n,x,it,1,k)
                        filename=formulae_str+"_a"+str(a)+"_b"+str(b)+"_n"+str(it)+"_x0"+str(x)+"_i"+str(n)+".png"
                        caption = "a="+str(a)+" b="+str(b)+" n="+str(n)+" x0="+str(x)+" i="+str(it)
                        plotting(fig, ax, y1,formulae_str,filename,caption)
                        

                else:
                    f=foo_evaluator(formulae_str,a,b,n,X0,len(X0),0,1)
                    g=foo_evaluator(formulae_str,a,b,n,X0,len(X0),0,k)
                    filename=formulae_str+"_a"+str(a)+"_b"+str(b)+"_n"+str(it)+"_i"+str(n)+".png"
                    caption = "a="+str(a)+" b="+str(b)+" n="+str(n)+" i="+str(it)
                    plotting(fig, ax, f,formulae_str,filename,caption)
                    plotting(fig, ax, g,formulae_str,filename,caption)
                    
                    if obs_flag:
                        plot_observation(fig,ax,data)
                    
                    if histo:
                        plot_hist(f,g,figh,axh,bind)
                    

