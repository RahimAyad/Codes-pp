import numpy as np
import matplotlib.pyplot as plt

Nx = 100                #size of points x in the lattice
Nt = 1000               #size of points t in the lattice

D = 1.0                 #diffusion constant
d_x = 0.01              #step of x
d_t = 6e-5              #step of t

x = np.arange(Nx)*d_x   #all the x's
r = d_t*D/d_x**2        #constant before the discretization term

#the Temperature set with the boundaries 
T = np.full(Nx,0.)      
T[0]=1.
T[-1]=0.


for i in range(1,Nt+1):
    T[1:-1] = T[1:-1] + r*(T[2:]- 2*T[1:-1] + T[:-2]) 

    if i %100 ==0: 
        plt.plot(x,T,label=f'{i*d_t}s')

plt.title(f'Heat equation D={D}and dt={d_t}')
plt.xlabel("x")
plt.ylabel("T")
# plt.legend()
plt.show()
