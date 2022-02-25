import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

D = 2.87
B = 0.01
theta = np.linspace(0,np.pi,501)
gu = 28

a = np.zeros(len(theta))
b = np.zeros(len(theta))
c = np.zeros(len(theta))

plot = plt.figure(1)
plt.title('Graph of f vs. $\Theta$ ($ B = 0.01 T$)')
plt.xlabel('$\Theta$ (radians)')
plt.ylabel('f(GHz)')

for i in range(len(theta)):
    A = np.array([[D+B*gu*np.cos(theta[i]),0,0],[0,0,0],[0,0,D-B*gu*np.cos(theta[i])]])
    BB = gu*B*np.sin(theta[i])*np.sqrt(1/2)*np.array([[0,1,0],[1,0,1],[0,1,0]])
    C = A+BB
    ev,EV = la.eig(C)
    a[i]=ev.real[0]
    b[i]=ev.real[1]
    c[i]=ev.real[2]
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

    plt.scatter(theta[i],a[i],s=1,color=col1)
    plt.scatter(theta[i], b[i],s=1, color=col2)
    plt.scatter(theta[i], c[i],s=1, color=col3)

plt.plot(theta,D*np.ones(len(theta)),'r--',label="|1>")
plt.plot(theta,np.zeros(len(theta)),'g--',label="|0>")
plt.plot(theta,D*np.ones(len(theta)),'b:',label="|-1>")
plt.legend()
plt.show()
'''
plot1 = plt.figure(1)
plt.title('Graph of f vs. $\Theta$ ($ B = 0.01 T$)')
plt.xlabel('$\Theta$ (radians)')
plt.ylabel('f(GHz)')
plt.plot(theta,D*np.ones(len(theta)),'b--')
plt.plot(theta,np.zeros(len(theta)),'g--')
plt.plot(theta,D*np.ones(len(theta)),'r:')
plt.plot(theta,a,'b',label='|1>')
plt.plot(theta,b,'g',label='|0>')
plt.plot(theta,c,'r',label='|-1>')
plt.legend()
plt.show()
'''




