import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100,1000)
y = np.sin(x)
z = np.cos(x)

plt.figure(1)
plt.plot(x,y)

plt.figure(2)
plt.plot(x,z)

plt.show()


