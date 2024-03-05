import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [200] #starting with 1 
N_0 = y0[0]

tend = 200
N = 1000

t = np.linspace(0,tend,N)

r = 0.05
lam1 = 0.04
def var(t):
    return (((r+lam1)/(r-lam1))*N_0*(np.exp(2*(r-lam1)*t)-np.exp((r-lam1)*t)))


plt.plot(t,var(t),color ='blue',label = f'lambda = {lam1} and r = {r} (theory)')


def gillespie(tmax, rate1, rate2):
    # Initialisation du temps et des compteurs de particules
    t = 0
    time_points = [t]
    particle_count = [N_0]  # Nombre initial de particules

    while time_points [-1]< tend:
        # Calculer le taux total de désintégration
        rate = np.abs(rate1 - rate2)
        total_rate = rate * particle_count[-1]

        # Vérifier si le taux total est non nul pour éviter la division par zéro
        if total_rate != 0:
            # Générer le temps jusqu'à la prochaine désintégration
            dt = np.random.exponential(1 / total_rate) 
     
        # Mettre à jour le temps et le nombre de particules
        t += dt
        time_points.append(t)
        particle_count.append(particle_count[-1] + 1)  # Une particule se désintègre

    return time_points, particle_count


mean_time = []
dt = 0.2
ttc = np.arange(0.0,tend,dt)
K = 0
n_p_s = []
n_p = [N_0]

for i in range (10):
    time_points1, particle_count1 = gillespie(tend, r ,lam1)
    # print(time_points1)
# Tracer les résultats
    # plt.step(time_points1, particle_count1,alpha=0.3)
    for i in range(len(ttc)):
        for j in range (0,len(time_points1)):
            K = (time_points1[j-1]-ttc[i])*(time_points1[j]-ttc[i])
            # print(K)
            if K < 0 and j!=0:
                n_p.append(N_0 + j)
    n_p_s.append(n_p)
    n_p = [N_0]


longueur_maximale = max(len(sous_liste) for sous_liste in n_p_s)

matrice_carrée = [sous_liste + [0] * (longueur_maximale - len(sous_liste)) for sous_liste in n_p_s]
particules_restante_carre = [[x**2 for x in sous_liste] for sous_liste in matrice_carrée]

particules_mean = np.mean(matrice_carrée, axis=0)
particules_restante_carre_mean = np.mean(particules_restante_carre, axis=0)

particules_mean_carre = [x**2 for x in particules_mean]

var = particules_restante_carre_mean - particules_mean_carre

T = np.linspace(0,tend,len(var))

plt.plot(T,var,label="numérique")
plt.xlabel('temps')
plt.ylabel('Variance')

plt.legend()
plt.show()