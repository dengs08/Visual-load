import numpy as np
import tensor as ts

def Cayley2R(a):
    '''
    Return the rotation tensor projection of Cayley parameters.
    
           1           T       ~    ~~
    R = --------[(1 + a a)I + 2a + 2aa]
    =        T        - - =
        1 + a a
            - -
    '''
    p1     = 1+np.vdot(a,a)
    a_skew = ts.skew_symm_mat(a)
    
    return 1./(p1)*((p1)*np.eye(3)+2.*a_skew+2*a_skew.dot(a_skew))

def Cayley2R_expand(a):
    '''
    Return the rotation tensor projection of Cayley parameters.
    
           1           T       ~    ~~
    R = --------[(1 + a a)I + 2a + 2aa]
    =        T        - - =
        1 + a a
            - -

    The tensor is calculated in expanded form.
    '''
    p1  = 1+np.vdot(a,a)
    
    R11 = 1 + a[0]**2 - a[1]**2 - a[2]**2
    R22 = 1 - a[0]**2 + a[1]**2 - a[2]**2
    R33 = 1 - a[0]**2 - a[1]**2 + a[2]**2
    
    R12 = 2*(a[0]*a[1] - a[2])
    R21 = 2*(a[0]*a[1] + a[2])
    
    R13 = 2*(a[0]*a[2] + a[1])
    R31 = 2*(a[0]*a[2] - a[1])
    
    R23 = 2*(a[1]*a[2] - a[0])    
    R32 = 2*(a[1]*a[2] + a[0])
    
    return np.array([[R11,    R12,  R13],
                     [R21,    R22,  R23],
                     [R31,    R32,  R33]]/p1)
