import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [1] 	#starting with 1 individual

tend = 500	#ending time	
N = 1000	#number of iterations

t = np.linspace(0,tend,N)

r = 0.05	#rate of birth
K = 1000 	#carrying capacity

params = [r,K]
#solve the ODE
def sim(Initial,t,params):
    
    x = Initial[0]  
    
    r = params[0]
    K = params[1]
    
    dxdt = r*x*(1-x/K) 
    
    return([dxdt])

y = odeint(sim,y0,t,args=(params,))
plt.title("Evolution of population of 1 cell with K=1000")
plt.grid(True)

plt.xlabel('time')
plt.ylabel('Population')
plt.legend()
plt.plot(t,y[:,0])
plt.show()
