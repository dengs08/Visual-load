from numpy import sin, cos, pi, array
import numpy as np
from Tensor import *
def R2e(R):
    '''
    Return Euler parameters determined by the rotation tensor.
    
                                T
        [ 1 + tr(R)       2axial (R)     ]
    T =          =                =
    =
        [ 2axial(R)  [1-tr(R)]I+2symm(R) ]
                 =         =  =       =
                 
              2     
           [ e    e e   e e   e e   ]
              0    0 1   0 2   0 3
                    2
           [e e    e    e e   e e   ]
             0 1    1    1 2   1 3
    T = 4                 2
    =      [e e   e e    e    e e   ]
             0 2   1 2    2    2 3
                                2
           [e e   e e   e e    e    ]
             0 3   1 3   2 3    3
    
    '''
    A = np.matrix(1.+np.trace(R))
    B = np.matrix(2*axial(R))
    C = np.matrix(2*axial(R)).getT()
    D = np.matrix((1.-np.trace(R))*np.eye(3)+2*symm(R))
    T = np.bmat([[A,B],[C,D]]).tolist()
    m = np.argmax(array([T[0][0],T[1][1],T[2][2],T[3][3]]))
    Delta_m = 2*np.sqrt(T[m][m])
    return np.array([T[0][m],T[1][m],T[2][m],T[3][m]]/Delta_m)
    
