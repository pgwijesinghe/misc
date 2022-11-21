import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

D = 2.87
B = 0.1
theta = np.linspace(0,np.pi,501)
gu = 28

a = np.zeros(len(theta))
b = np.zeros(len(theta))
c = np.zeros(len(theta))
d = np.zeros(len(theta))
e = np.zeros(len(theta))
f = np.zeros(len(theta))


for i in range(len(theta)):
    A = np.array([[D+B*gu*np.cos(theta[i]),0,0],[0,0,0],[0,0,D-B*gu*np.cos(theta[i])]])
    BB = gu*B*np.sin(theta[i])*np.sqrt(1/2)*np.array([[0,1,0],[1,0,1],[0,1,0]])
    C = A+BB
    ev,EV = la.eig(C)
    a[i]=ev.real[0]
    b[i]=ev.real[1]
    c[i]=ev.real[2]
    d[i] = EV[0,1]
    e[i] = abs(EV[1,1])**2
    f[i] = abs(EV[2,1])**2
print(d)
plot = plt.figure(1)
plt.plot(theta,d)
plt.plot(theta,e)
plt.plot(theta,f)

plt.show()






