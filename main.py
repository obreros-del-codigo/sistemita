import matplotlib.pyplot as plt 
from sympy import *
import matplotlib
import numpy as np

import sys
from plot import plotting
from variable_input import *
from iterations import *
from graph import *

quererplot=input("¿Quieres que se guarde una foto de tu ecuación? [y/n]") 

inputs,formulae_str=foo_input()
print(inputs)
print(formulae_str)

n,a,b,x0,i=inputs


z,x,y=foo_iterations(a,b,x0,i,n,formulae_str)

foo_graph(z,y,x)


