from numpy import array
import numpy as np
import tensor as ts


def A(e):
    '''
                                                    ^
    Return the 4*4 matrice operator A of quaternion e.
                     T
      ^    [e      -e     ]
    A(e) =   0      -
    =                   ~
           [e     e I + e ]
            -      0=
    '''
    return array([[e[0],-e[1],-e[2],-e[3]],
                  [e[1], e[0],-e[3], e[2]],
                  [e[2], e[3], e[0],-e[1]],
                  [e[3],-e[2], e[1], e[0]]])

def B(e):
    '''
                                                    ^
    Return the 4*4 matrice operator B of quaternion e.
                     T
      ^    [e      -e     ]
    B(e) =   0      -
    =                   ~
           [e     e I - e ]
            -      0=
    '''
    return array([[e[0],-e[1],-e[2],-e[3]],
                  [e[1], e[0], e[3],-e[2]],
                  [e[2],-e[3], e[0], e[1]],
                  [e[3], e[2],-e[1], e[0]]])

def C(e):
    '''
                                                    ^
    Return the 4*4 matrice operator C of quaternion e.
                     T
      ^    [e       e     ]
    C(e) =   0      -
    =                   ~
           [e   -e I - e ]
            -      0=
    '''
    return array([[e[0], e[1], e[2], e[3]],
                  [e[1],-e[0], e[3],-e[2]],
                  [e[2],-e[3],-e[0], e[1]],
                  [e[3], e[2],-e[1],-e[0]]])

def D(e):
    '''
                                                      ^
    Return the 4*4 bi-linear operator D of quaternion e.
                     
      ^      ^  T       T ^   ^      ^   ^
    D(e) = A(e)B (e) = B (e)A(e) = C(e)C(e)
    =      =   =       =    =      =   = 

                                                     ^
    Which can be verified that for a unit quaternion e
                     T
      ^    [1       0     ]
    D(e) =          -
    =                 ^
           [0       R(e)  ]
            -       =
    
    '''
    return C(e).dot(C(e))

def R(e):
    '''
    Return the rotation tensor 
                  ~    ~~
    R(e) = I + 2e e + 2ee
    = -    =     0
    '''
    e_skew = ts.skew_symm_mat([e[1],e[2],e[3]])
    return np.eye(3)+2*e[0]*e_skew+2*e_skew.dot(e_skew)
    
