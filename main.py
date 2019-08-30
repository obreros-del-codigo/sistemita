from plot import plotting
from variable_input import *
from iterations import *


quererplot=input("¿Quieres que se guarde una foto de tu ecuación? [y/n]") 

formulae_str,A,B,N,X0,it=foo_input()
print(A,B,N,X0,it)

foo_iterations(formulae_str,A,B,N,X0,int(it))



