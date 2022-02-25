import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
from scipy.sparse import spdiags

N = 100
h = 0.0001

e = np.ones(N)
A = spdiags([-e,2*e,-e], [-1,0,1], N, N).toarray()

A[0,:]=np.zeros(N)
A[0,0]=1
A[N-1,:]=np.zeros(N) 
A[N-1,N-1]=1

p = np.zeros(N)
m = int((N/2)-1)
p[m] = -1/h**3

b = (h**2)*p*(1e-19/(1e-9*1e-12))

b[0] = 0
b[N-1] = 0

y = np.linalg.solve(A,b)

x = np.linspace(-2,2,N)*1e-9

plt.plot(x,y)
plt.show()


