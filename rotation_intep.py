from Wiener_Milenkovic import *
from shapefunction import *
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')

n = [[0.3049,0.6097,0.7316],[0.3262,0.6461,0.6900],
     [0.3193,0.6095,0.7256],[0.3105,0.5485,0.7763]]
phi = [145,160,170,181]
s = np.linspace(-1.0,1.0,100)

def pltc(ax,s,c,c_node,num,name):
    ax.plot(s,c[:,num],[-1.0,-1./3,1./3,1.0],c_node[:,num],'o')


def Intep(WithRescal):
    c_node = []
    for i, p in enumerate(phi):
        if WithRescal == True:
            c_node.append(c_d_rescal(n[i][:],p))
        else:
            c_node.append(c_d(n[i][:],p))
    c_node = np.matrix(c_node)
    c = u(s,c_node)
    c_p = dudalpha(s,c_node)
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
    pltc(ax1,s,c,c_node,0,'c1')
    pltc(ax2,s,c,c_node,1,'c2')
    pltc(ax3,s,c,c_node,2,'c3')
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
    pltc(ax1,s,c_p,c_node,0,'c1')
    pltc(ax2,s,c_p,c_node,1,'c2')
    pltc(ax3,s,c_p,c_node,2,'c3')
    
Intep(False)
Intep(True)

plt.show()
