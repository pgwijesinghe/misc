import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

D = 2.87
B = np.linspace(0,.05,501)
theta = 74
gu = 28

a = np.zeros(len(B))
b = np.zeros(len(B))
c = np.zeros(len(B))
Ea = np.zeros(len(B))
Eb = np.zeros(len(B))
Ec = np.zeros(len(B))

plot=plt.figure(1)
plt.title('Graph of f vs. B ($ \Theta = 0$)')
plt.xlabel('B(T)')
plt.ylabel('f(GHz)')

for i in range(len(B)):
    A = np.array([[D+B[i]*gu*np.cos(theta),0,0],[0,0,0],[0,0,D-B[i]*gu*np.cos(theta)]])
    BB = gu*B[i]*np.sin(theta)*np.sqrt(1/2)*np.array([[0,1,0],[1,0,1],[0,1,0]])
    C = A+BB
    ev,EV = la.eig(C)
    a[i]=ev.real[0]
    b[i]=ev.real[1]
    c[i]=ev.real[2]

    Ea[i] = EV[0,2]**2
    Eb[i] = EV[1,2]**2
    Ec[i] = EV[2,2]**2

    aa = int(255*(EV[0,0]**2))
    bb = int(255*(EV[1,0]**2))
    cc = int(255*(EV[2,0]**2))
    dd = int(255*(EV[0,1]**2))
    ee = int(255*(EV[1,1]**2))
    ff = int(255*(EV[2,1]**2))
    gg = int(255*(EV[0,2]**2))
    hh = int(255*(EV[1,2]**2))
    ii = int(255*(EV[2,2]**2))

    col1 = '#%02x%02x%02x' % (aa,bb,cc)
    col2 = '#%02x%02x%02x' % (dd,ee,ff)
    col3 = '#%02x%02x%02x' % (gg,hh,ii)

    # plt.scatter(B[i],a[i],s=1,color=col1)
    # plt.scatter(B[i], b[i],s=1, color=col2)
    # plt.scatter(B[i], c[i],s=1, color=col3)

plt.plot(B, D*np.ones(len(B)), 'r--', label="|1>")
plt.plot(B, np.zeros(len(B)), 'g--', label="|0>")
plt.plot(B, D*np.ones(len(B)), 'b:', label="|-1>")
plt.legend()

plot1 = plt.figure(2)
plt.plot(B, Ea,'r', label='|1>')
plt.plot(B, Eb,'g', label='|0>')
plt.plot(B, Ec,'b', label='|-1>')

plt.show()

'''    
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
'''




