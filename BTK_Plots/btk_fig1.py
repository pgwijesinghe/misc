import matplotlib.pyplot as plt
import numpy as np

# global variables
delta = 20
emax = 100
Z = [0,0.3,1,3]

fig = plt.figure() # initialize the main figure

# defining x-axis
E1 = np.linspace(0,delta)
E2 = np.linspace(delta,emax)

for j in range(len(Z)): # looping through Z

    fig.add_subplot(str(221+j))

    # 0 < E < delta
    A1=np.zeros(len(E1))
    B1=np.zeros(len(E1))
    C1=np.zeros(len(E1))
    D1=np.zeros(len(E1))

    for i in range(len(E1)): 
        A1[i] = (delta**2)/(E1[i]**2 + (delta**2-E1[i]**2)*(1+2*Z[j]**2)**2)
        B1[i] = 1 - A1[i]
    
    plt.plot(E1,A1,E1,B1,E1,C1,E1,D1)

    # delta < E < Emax
    A2=np.zeros(len(E2))
    B2=np.zeros(len(E2))
    C2=np.zeros(len(E2))
    D2=np.zeros(len(E2))
    u2,v2,g2 = np.zeros(len(E2)),np.zeros(len(E2)),np.zeros(len(E2))

    for i in range(len(E2)):
        u2[i] =  .5*(1+((E2[i]**2-delta**2)/(E2[i]**2))**.5)
        v2[i] = 1 - u2[i]
        g2[i] = (u2[i] + (Z[j]**2)*(u2[i]-v2[i]))**2

        A2[i] = (u2[i]*v2[i])/g2[i]
        B2[i] = (((u2[i]-v2[i])**2)*(Z[j]**2)*(1+Z[j]**2))/g2[i]
        C2[i] = ((u2[i]-v2[i])*(u2[i])*(1+Z[j]**2))/g2[i]
        D2[i] = ((u2[i]-v2[i])*(v2[i])*(1+Z[j]**2))/g2[i]

    plt.plot(E2,A2,E2,B2,E2,C2,E2,D2)

plt.show()