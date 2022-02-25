import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

D = 2.87
B = np.linspace(0,.2,101)
theta = 1
gu = 28

a = np.zeros(len(B))
b = np.zeros(len(B))
c = np.zeros(len(B))

for i in range(len(B)):
    A = np.array([[D+B[i]*gu,0,0],[0,0,0],[0,0,D-B[i]*gu]])
    ev,EV = la.eig(A)
    a[i]=ev.real[0]
    b[i]=ev.real[1]
    c[i]=ev.real[2]

plot1 = plt.figure(1)
plt.title('Graph of f vs. B ($ \Theta = 0$)')
plt.xlabel('B(T)')
plt.ylabel('f(GHz)')
plt.plot(B,D*np.ones(len(B)),'b--')
plt.plot(B,np.zeros(len(B)),'g--')
plt.plot(B,D*np.ones(len(B)),'r:')
plt.plot(B,a,'b',label='|1>')
plt.plot(B,b,'g',label='|0>')
plt.plot(B,c,'r',label='|-1>')
plt.legend()
plt.show()





