#EXCESS CURRENT

import numpy as np 
from scipy import integrate
import matplotlib.pyplot as plt

e = -1
delta = 20
Z = np.linspace(0,2)
I = np.zeros(len(Z))

for i in range(len(Z)):

    Binf = (Z[i]**2/(1+Z[i]**2))

    func1 = lambda E1: 2*(delta**2)/(E1**2 + (delta**2-E1**2)*(1+2*Z[i]**2)**2) - 1 + Binf #E < delta

    def func2(E2):  # E > delta
        u2 =  .5*(1+((E2**2-delta**2)/(E2**2))**.5)
        v2 = 1 - u2
        g2 = (u2 + (Z[i]**2)*(u2-v2))**2

        A = (u2*v2)/g2
        B = (((u2-v2)**2)*(Z[i]**2)*(1+Z[i]**2))/g2

        f = A - B + Binf

        return f

    I[i] = (1/e/(1-Binf))*(integrate.quad(func1,0,delta)[0] + integrate.quad(func2,delta,np.inf)[0])

fig = plt.figure()
plt.plot(Z,e*I/delta)
plt.show()