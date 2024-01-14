import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N_initial = 600
lam = 5

n = 1000
tend = 1.6
t = np.linspace(0,tend,n)

def function(N_initial,t):
    N = N_initial
    
    dNdt= -lam*N
    return(dNdt)

y = odeint(function, N_initial, t)


def gillespie(tmax, rate):
    t = 0
    time_points = [t]
    particle_count = [N_initial]  # Nombre initial de particules

    while t < tmax:
        # Calculer le taux total de désintégration
        total_rate = rate * particle_count[-1]

        # Générer le temps jusqu'à la prochaine désintégration
        dt = -np.log(np.random.uniform()) / total_rate
        print(dt)
        # Mettre à jour le temps et le nombre de particules
        t += dt
        time_points.append(t)
        particle_count.append(particle_count[-1] - 1)  # Une particule se désintègre

    return time_points, particle_count

# Exécuter la simulation de Gillespie
time_points1, particle_count1 = gillespie(tend, lam)
time_points2, particle_count2 = gillespie(tend, lam)
time_points3, particle_count3 = gillespie(tend, lam)

# Tracer les résultats
plt.step(time_points1, particle_count1, label='Population1')
plt.step(time_points2, particle_count2, label='Population2')
plt.step(time_points3, particle_count3, label='Population3')

plt.grid(True)
plt.plot(t,y,"--",color="black",label="Analytical solution")

plt.legend()
plt.xlabel('Time')
plt.ylabel('Number of particules')

plt.show()
