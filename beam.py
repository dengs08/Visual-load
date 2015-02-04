# The cantilevered beam under tip loading
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()

E_G = 2.6   # E/G, E: Young's modulus; G: shear modulus
L_h = 10.0  # L/h, L: length of beam;  h: cross section hight
N = 12
P = 4
M = 0.0
a_2 = 1.0/12.0*(1.0/L_h)**2
s_2 = 1.0/10.0*E_G*(1.0/L_h)**2
u1t = 0.0
u2t = 0.0

alpha = 0.9

# solve the system dy/dt = f(y, t)
def f(y, t):
        u1 = y[0]
        u2 = y[1]
        th = y[2]
        ct = np.cos(th)
        st = np.sin(th)
        # the model equations (see Munz et al. 2009)
        f0 = ct-1.0+N*(a_2*ct**2+s_2*st**2)-P*(s_2-a_2)*st*ct
        f1 = st    +P*(a_2*st**2+s_2*ct**2)-N*(s_2-a_2)*st*ct
        f2 = M     +P*(1-t+u1t-u1)         -N*(u2t-u2)
        return [f0, f1, f2]

# initial conditions
y0 = [0.0, 0.0, 0.0]       # initial condition vector
l  = np.linspace(0.0, 1., 1000)   # time grid

for i in range(1,100):
        # solve the DEs
        soln = odeint(f, y0, l)
        U1 = soln[:, 0]
        U2 = soln[:, 1]
        TH = soln[:, 2]
        u1t = alpha*u1t + (1.0-alpha)*U1[-1]
        u2t = alpha*u2t + (1.0-alpha)*U2[-1]

x0_1 = l
x0_2 = np.linspace(0.0, 0., 1000)   # time grid
# plot results
plt.figure()
plt.plot(x0_1+U1,x0_2+U2, label='shape')
plt.xlabel('length')
plt.ylabel('u2')
plt.title('Deflected shape of the beam')
plt.legend(loc=0)
