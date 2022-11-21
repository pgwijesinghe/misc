import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

D = 2.87
B = 0.1
theta = np.linspace(0,np.pi)
gu = 28

a = np.zeros(len(theta))
b = np.zeros(len(theta))
c = np.zeros(len(theta))

for i in range(len(theta)):
    A = np.array([[D+B*np.cos(theta[i])*gu,0,0],[0,0,0],[0,0,D-B*np.cos(theta[i])*gu]])
    ev,EV = la.eig(A)
    a[i]=ev.real[0]
    b[i]=ev.real[1]
    c[i]=ev.real[2]

plot1 = plt.figure(1)
plt.title('Graph of f vs. $\Theta$ ($ B = 10 mT$)')
plt.xlabel('$\Theta (radians)$')
plt.ylabel('f(GHz)')
plt.plot(theta,D*np.ones(len(theta)),'b--')
plt.plot(theta,np.zeros(len(theta)),'g--')
plt.plot(theta,D*np.ones(len(theta)),'r:')
plt.plot(theta,a,'b',label='|1>')
plt.plot(theta,b,'g',label='|0>')
plt.plot(theta,c,'r',label='|-1>')
plt.legend()
plt.show()





