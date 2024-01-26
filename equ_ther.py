import numpy as np
import matplotlib.pyplot as plt

N = 100			#time and space iterations 
x = np.linspace(0,1,N)	#x axes 
dx = x[1]-x[0]		#space step
dx2 = dx**2		#space step squared
U = np.zeros(N)		#table that will collect the resolution
laplacien = np.zeros(N)	#laplacian
dt = 6e-5		#time step

#boundary conditions
U[0] = 1
U[N-1] = 0
D = 1.0
print (U)

alpha = D*dt/dx2 	#prefactor
#resolution of the equation explicitly
for i in range (1000):
    for k in range (1,N-1):
        laplacien[k] = (U[k+1]-2*U[k]+U[k-1])/dx2
    for k in range (1,N-1):
        U[k] += dt*D*laplacien[k]

plt.plot(x,U,label='Diffusion equation')
plt.title('Discritisation equation de diff 1D ')
plt.xlabel('x')
plt.ylabel('U')
plt.legend()
plt.grid(True)
plt.show()

