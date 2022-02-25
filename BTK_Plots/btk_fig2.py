import numpy as np 
from scipy import integrate
import matplotlib.pyplot as plt

e = -1
delta = 20
Z = 1.5
Ef = 100 

v = np.linspace(0,50)
I = np.zeros(len(v))

for i in range(len(v)):

    func1 = lambda E1: 2*(delta**2)/(E1**2 + (delta**2-E1**2)*(1+2*Z**2)**2) #E < delta
    
    def func2(E2):  # E > delta
        u2 =  .5*(1+((E2**2-delta**2)/(E2**2))**.5)
        v2 = 1 - u2
        g2 = (u2 + (Z**2)*(u2-v2))**2

        A = (u2*v2)/g2
        B = (((u2-v2)**2)*(Z**2)*(1+Z**2))/g2

        f = 1 - A - B

        return f

    func3 = lambda E3: 2*(delta**2)/((E3+e*v[i])**2 + (delta**2-(E3+e*v[i])**2)*(1+2*Z**2)**2) #E < delta
    
    def func4(E4):  # E > delta
        E = E4 + e*v[i]
        u2 =  .5*(1+((E**2-delta**2)/(E**2))**.5)
        v2 = 1 - u2
        g2 = (u2 + (Z**2)*(u2-v2))**2

        A = (u2*v2)/g2
        B = (((u2-v2)**2)*(Z**2)*(1+Z**2))/g2

        f = 1 - A - B

        return f

    I1 = integrate.quad(func3,-np.inf,delta-e*v[i])[0] - integrate.quad(func1,-np.inf,delta)[0]
    I2 = integrate.quad(func4,delta-e*v[i],Ef-e*v[i])[0] - integrate.quad(func2,delta,Ef)[0]
    I[i] = I1 + I2

fig = plt.figure()
plt.plot(e*v/delta,e*I/delta)
plt.show()