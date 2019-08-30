import matplotlib.pyplot as plt
import pylab
def plotting(fig, ax,y1,title,filename,caption):
    time=[]
    weight=1e-12
    for i,v in enumerate(y1):
        y1[i]*=weight
    mitosis=3
    tiempo=0
    for i in range(len(y1)):
        time.append(tiempo)
        tiempo+=mitosis
    ax.plot(time,y1, label=caption)
    ax.set_yscale('log')
    ax.set(xlabel='Hours',ylabel='Weight',
           title=title)
    ax.grid()
    #pylab.legend(loc='upper left')

    fig.savefig(title+'.png')
    
