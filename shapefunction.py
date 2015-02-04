import numpy as np

def h1(s):
    return 9.0/16.0*(np.square(s)-1./9.)*(1-s)

def h2(s):
    return 9.0/16.0*(np.square(s)-1./9.)*(1+s)

def h3(s):
    return -27./16.*(1.-np.square(s))*(s-1./3.)

def h4(s):
    return  27./16.*(1.-np.square(s))*(s+1./3.)

def dh1ds(s):
    return 9.0/16.0*(2*s-3*np.square(s)+1./9)

def dh2ds(s):
    return 9.0/16.0*(2*s-np.square(s)+1./9)

def dh3ds(s):
    return -27.0/16.0*(2./3*s-3*np.square(s)+1.)

def dh4ds(s):
    return  27.0/16.0*(-2./3*s-3*np.square(s)+1.)

def u(s,u_node):
    return np.matrix(h1(s)).getT()*u_node[0,:]+\
   np.matrix(h2(s)).getT()*u_node[3,:]+\
   np.matrix(h3(s)).getT()*u_node[1,:]+\
   np.matrix(h4(s)).getT()*u_node[2,:]

def dudalpha(s,u_node):
    duds =  np.matrix(dh1ds(s)).getT()*u_node[0,:]+\
   np.matrix(dh2ds(s)).getT()*u_node[3,:]+\
   np.matrix(dh3ds(s)).getT()*u_node[1,:]+\
   np.matrix(dh4ds(s)).getT()*u_node[2,:]
    return duds


