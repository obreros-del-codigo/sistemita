import matplotlib.pyplot as plt 

def foo_graph(zl,yl,xl):
    gix,ax=plt.subplots()    
    ax.set_yscale("log")
    plt.plot(xl)
    plt.plot(yl)
    plt.plot(zl)
    plt.show()
    if quererplot == "y":
        plotting(xl,yl,zl,formulae_str[:-1])
    
