import numpy as np
import matplotlib.pyplot as plt

T = 2000
n = 100
t=np.linspace(0,T,n)
y=np.cos(2*np.pi*t*(2760+(40/2000)*t))

plt.plot(t,y)
plt.show()


