import matplotlib.pyplot as plt #load plot library

x=float(input("Numero:"))
y=float(input("Numero:"))
z=float(input("Numero:"))
n=int(input("iteraciones"))    
      
      
xl=[x]
yl=[y]
zl=[z]

for i in range(n):
    x=x*x+1
    y=y*y+1
    z=z*z+1
    xl.append(x)
    yl.append(y)
    zl.append(z)
gix,ax=plt.subplots()    
ax.set_yscale("log")
plt.plot(xl)
plt.plot(yl)
plt.plot(zl)
plt.show()



    
