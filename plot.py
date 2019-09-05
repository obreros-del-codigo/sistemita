import matplotlib.pyplot as plt
import pylab
def plotting(fig, ax,y1,title,filename,caption):
    
    ax.plot(y1, label=caption)
    #ax.set_yscale('log')
    ax.set(xlabel='i',ylabel='$x_i$',
           title=title)
    ax.grid()
    #pylab.legend(loc='upper left')

    fig.savefig(title+'.png')
    
