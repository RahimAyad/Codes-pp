import numpy as np
import matplotlib.pyplot as plt


X_initial = 10.    #initial population
Y_initial = 2.      #initial population

wb1 = 1.1           #rate of birth for prey
wb2 = 0.1           #rate of birth for predators
wd1 = 0.4          #rate of death for prey
wd2 = 0.4           #rate of death for predators

tend = 50           #time
d_t = 0.0005
N = int(tend/d_t) 

X = [X_initial] *N
Y = [Y_initial] *N
t = [0] *N


t1 = np.linspace(0,tend,N)

for i in range(0,N-1):
    X[i+1] = X[i] + (wb1 * X[i] - wd1 * X[i] * Y[i]) * d_t
    Y[i+1] = Y[i] + (wb2 * Y[i] * X[i] - wd2 * Y[i]) * d_t
    t[i+1] = t[i] + d_t

plt.title("Evolution of population of 10 Prey and 2 Predator")
plt.grid(True)
plt.plot(t,X,color="purple",label="prey")
plt.plot(t,Y,color="darkorange",label="predators")
plt.xlabel('time')
plt.ylabel('Population')
plt.legend()
plt.show()