import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


P0_initial = 1/2.   #initial probability of being in spot 0
P1_initial = 0.    #initial probability of being in spot 1
P2_initial = 1/2.    #initial probability of being in spot 2
InitialP = [P0_initial,P1_initial,P2_initial]

w01 = 0.             #rate to pass from spot 1 to 0
w02 = 1/3            #rate to pass from spot 2 to 0
w10 = 0.5            #rate to pass from spot 0 to 1
w20 = 0              #rate to pass from spot 0 to 2
w12 = 1
w21 = 1/3

N = 1000
tend = 12.
t = np.linspace(0,tend,N)


params = [w01, w10, w02, w20, w12, w21]

def sim(InitialP, t, params):

    P0 = InitialP[0]
    P1 = InitialP[1]
    P2 = InitialP[2]


    w01 = params[0]
    w10 = params[1]
    w02 = params[2]
    w20 = params[3]
    w12 = params[4]
    w21 = params[5]


    dP0dt = w02 * P2 + w01 * P1 - w20 * P0 - w10 * P0
    dP1dt = w10 * P0 + w12 * P2 - w21 * P1 - w01 * P1
    dP2dt = w20 * P0 + w21 * P1 - w12 * P2 - w02 * P2
    
    return([dP0dt, dP1dt, dP2dt])


y = odeint(sim, InitialP, t, args=(params,))



plt.plot(t,y[:,0],"--", color="b",label="P0,Slepping")
plt.plot(t,y[:,1], color="green",label="P1,playing")
plt.plot(t,y[:,2],":", color="black",label="P2,Eating")
plt.title("Evolution of probabilities")
plt.grid(True)

plt.xlabel('time')
plt.ylabel('Probability')
plt.legend()
plt.show()
