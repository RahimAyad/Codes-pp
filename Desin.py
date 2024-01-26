import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N_initial = 600			#initial population	
lam = 5				#parameter lambda

n = 1000			#number of subtimes (how many dt) 
tend = 1.6			#end time
t = np.linspace(0,tend,n)	#our time

def function(N_initial,t):	#resolution of the ODE
    N = N_initial
    
    dNdt= -lam*N
    return(dNdt)

y = odeint(function, N_initial, t)


def gillespie(tmax, rate):	#gillespie to take random moments 
    t = 0
    time_points = [t]
    particle_count = [N_initial]  #initial number of particules

    while t < tmax:
        #Total rate of desintegration 
        total_rate = rate * particle_count[-1]

        #generate the time until the next desintegration
        dt = -np.log(np.random.uniform()) / total_rate
        print(dt)
        #update the number of particules 
        t += dt
        time_points.append(t)
        particle_count.append(particle_count[-1] - 1)  # Une particule se désintègre

    return time_points, particle_count


time_points1, particle_count1 = gillespie(tend, lam)
time_points2, particle_count2 = gillespie(tend, lam)
time_points3, particle_count3 = gillespie(tend, lam)


plt.step(time_points1, particle_count1, label='Population1')
plt.step(time_points2, particle_count2, label='Population2')
plt.step(time_points3, particle_count3, label='Population3')

plt.grid(True)
plt.plot(t,y,"--",color="black",label="Analytical solution")

plt.legend()
plt.xlabel('Time')
plt.ylabel('Number of particules')

plt.show()
