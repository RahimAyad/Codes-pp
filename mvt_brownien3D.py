import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
N = 1000
t1 = np.random.randint(2, size=N) - (1/2) 
t2 = np.random.randint(2, size=N) - (1/2) 
t3 = np.random.randint(2, size=N) - (1/2) 
x = [sum(t1[:i+1]) for i in range(len(t1))]
y = [sum(t2[:i+1]) for i in range(len(t2))]
z = [sum(t3[:i+1]) for i in range(len(t3))]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracez les points en 3D
plt.plot(x, y, z)

# Personnalisez le graphique
ax.set_xlabel(' X')
ax.set_ylabel(' Y')
ax.set_zlabel(' Z')
plt.title(" 3 D")
plt.grid(True)
plt.show()