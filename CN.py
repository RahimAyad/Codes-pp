import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

Nx = 100                #size of points x in the lattice
Nt = 1000               #size of points t in the lattice

D = 1.0                 #diffusion constant
d_x = 0.01              #step of x
d_t = 6e-5              #step of t

x = np.arange(Nx)*d_x   #all the x's
r = d_t*D/d_x**2        #constant before the discretization term

#the Temperature set with the boundaries 
T = np.full(Nx,0.0)      
T[0]=1.
T[-1]=0.

#set the matrix A and with the diagonals and every value on each side
A = np.zeros((3,Nx-2))
A[0,1:]=-r
A[1,:]=1+2.0*r
A[2,:-1]=-r

#set the matrix B with the same 
B = np.zeros(Nx-2)
B = r*T[2:]+(1-2.0*r)*T[1:-1]+r*T[:-2]
B[0]=B[0]+r*T[0]
B[-1]=B[-1]+r*T[-1]

#Crank-Nicholson implementation
for i in range(Nt+1):
    T[1:-1]=solve_banded((1,1),A,B)  #function to solve tridiagonal matrix Ax=B (1,1) means that the matrix have values before and after the diagonal
    B = r*T[2:]+(1-2.0*r)*T[1:-1]+r*T[:-2]
    B[0]=B[0]+r*T[0]
    B[-1]=B[-1]+r*T[-1]
    if i % 100 ==0 :
        plt.plot(x,T,label=f"{i*d_t}s")

plt.title(f'Heat equation D={D}and dt={d_t}')
plt.xlabel("x")
plt.ylabel("T")
plt.legend()
plt.show()