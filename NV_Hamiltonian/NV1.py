import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

D = 2.87  # GHz
B = np.linspace(0,.02,500)  # Tesla
theta = 35*np.pi/180  # radians
gu = 28  # GHz/Tesla
ev0, ev1, ev2 = [], [], []
E20, E10 = [], []

for i in range(len(B)):
    H1 = D*np.array([[1, 0, 0], [0, 0, 0], [0, 0, 1]])  # D*(Sz)^2
    H2 = gu*(B[i]*np.sin(theta)*np.sqrt(1/2)*np.array([[0,1,0],[1,0,1],[0,1,0]]) + B[i]*np.cos(theta)*np.array([[1,0,0],[0,0,0],[0,0,-1]]))  # gu(BxSx + BzSz)
    H = H1 + H2  # final hamiltonian for specific B/theta

    ev_sorted = np.sort(la.eig(H)[0])  # sorted eigenvalues of the hamiltonian

    ev0.append(ev_sorted.real[0])  # defines the E0 level
    ev1.append(ev_sorted.real[1])  # defines the E1 level
    ev2.append(ev_sorted.real[2])  # defines the E2 level
    
    E10.append(ev_sorted.real[1] - ev_sorted.real[0])  # transition between E1 and E0
    E20.append(ev_sorted.real[2] - ev_sorted.real[0])  # transition between E2 and E0

plot=plt.figure(1)  
plt.title('Graph of f vs. B ($ \Theta = 74 deg$)')
plt.xlabel('B(T)')
plt.ylabel('f(GHz)')
plt.plot(B,ev0,'r',B,ev1,'g',B,ev2,'b')
plt.show()

plot=plt.figure(2)
plt.title('Graph of Transition Energies (E20 and E10) ($ \Theta = 35 deg$)')
plt.xlabel('B(T)')
plt.ylabel('f(GHz)')
plt.plot(B,E20,label='E20')
plt.plot(B,E10,label='E10')
plt.hlines(2.47,B[0],B[-1],linestyles='dashed',colors='red',label='2.47 GHz')
plt.legend()
plt.show()
