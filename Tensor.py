import numpy as np

def skew_symm_mat(a):
    '''
    Return the skew-symmetric matrix of vector a.
    
    ~   [    0, -a[2],  a[1]]
    a = [ a[2],     0, -a[0]]
        [-a[1],  a[0],     0]
    '''
    return np.array([[0,    -a[2],  a[1]],
                     [a[2],     0, -a[0]],
                     [-a[1], a[0],  0   ]])

def axial(A):
    '''
    Return the axial vector a associated with a second-order tensor A.
    
        1[ A[3][2]-A[2][3]]
    a = -[ A[1][3]-A[3][1]]
    -   2[ A[2][1]-A[1][2]]
    '''
    return 0.5*np.array([A[2][1]-A[1][2],A[0][2]-A[2][0],A[1][0]-A[0][1]])        

def symm(A):
    '''
    Return the symmetric part of tensor A.
    
                    T
               A + A
               =   =
    symm(A) = -------
                 2
    '''
    return 0.5*np.array([[2*A[0][0]      ,  A[0][1]+A[2][1],  A[0][2]+A[2][0]],
                         [A[0][1]+A[2][1],        2*A[1][1],  A[1][2]+A[2][1]],
                         [A[0][2]+A[2][0],  A[1][2]+A[2][1],         2*A[2][2]]])
