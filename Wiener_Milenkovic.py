import numpy as np

def c(n,phi):
    '''
    Return the Wiener-Milenkovic parameter c for given unit vector and angles.
    
         -     phi
    c = 4n tan --- 
    -           4
    '''
    coef = 4.*np.tan(phi/4)
    return [coef*ni for ni in n]

def c_d(n,phi):
    '''
    Return the Wiener-Milenkovic parameter c for given unit vector and angle.
    Angle is in degree form.
    
         -     phi
    c = 4n tan --- 
    -           4
    '''
    coef = 4.*np.tan(phi/(4.*180.)*np.pi)
    return [coef*ni for ni in n]

def c_d_rescal(n,phi):
        coef = 4.*np.tan(phi/(4.*180.)*np.pi)
        if 180<np.abs(phi)<360:
            nu = np.square(np.cos(phi/4.))
            coef *=-(nu)/(1-nu)
            return [coef*ni for ni in n]
        else:
            return [coef*ni for ni in n]
        
