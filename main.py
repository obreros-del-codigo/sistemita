import matplotlib.pyplot as plt 
from sympy import *
import matplotlib
import numpy as np
import sys
from plot import plotting
quererplot=input("¿Quieres que se guarde una foto de tu ecuación? [y/n]") 
xf=0.1
yf=1.0
zf=10.0
file_flag = False
formulae_str = 'x'
equation_flag=False
n=len(sys.argv)

for i in range(n):
    if '-f' in sys.argv[i]:
        file_flag =True
        filename=sys.argv[i+1]
    if '-e' in sys.argv[i]:
        equation_flag =True
        formulae_str=sys.argv[i+1]    
    
if file_flag:
    with open('formulae.dat') as f:
        formulae=f.readlines()
        formulae_str=formulae[0]
        print("Using archive mode with "+formulae_str)
if equation_flag:
    print("Using equation "+formulae_str)

      
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
if quererplot == "y":
    plotting(xl,yl,zl,formulae_str[:-1])
