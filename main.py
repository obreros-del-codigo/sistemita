import matplotlib.pyplot as plt 
from sympy import *
import matplotlib
import numpy as np
xf=0.1
yf=1.0
zf=10.0
with open('formulae.dat') as f:
    formulae=f.readlines()
    formulae_str=formulae[0]
x = Symbol("x")
y=sympify(formulae_str)
yprime=y.diff(x)
f=lambdify(x,y,"numpy")

range=range(7)

      
xl=[]
yl=[]
zl=[]
for i in range:
    zf = f(zf)
    zl.append(zf)
for i in range:
    xf = f(xf)
    xl.append(xf)
for i in range:
    yf = f(yf)
    yl.append(yf)
gix,ax=plt.subplots()    
ax.set_yscale("log")
plt.plot(xl)
plt.plot(yl)
plt.plot(zl)
plt.show()
