import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
import time

temps_debut = time.time()

Histoires = 10000

N = 1000			#number of iterations	
T = 40				#Ending time
a = 0.2				#rate 
dt = T/N			#time step
p = a * dt			#probability
number_clicks_histories = [] 	#table to stock the clicks	


for j in range (Histoires):
    number_clicks_dt = np.zeros(N)
    for i in range (N):  
        if np.random.uniform(0,1) < p:		#We add +1 click given our probability
            number_clicks_dt[i]+= 1 
    number_clicks_histories.append(sum(number_clicks_dt))	#we count all the clicks 

# print (np.mean(number_clicks_histories))


# the bins should be of integer width, because poisson is an integer distribution
bins = np.arange(len(set(number_clicks_histories))) - 0.5
entries,bin_edges,patches = plt.hist(number_clicks_histories, bins=bins, density=True, label='Data')

# calculate bin centers
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

#we can also use a fit function
def fit_function(k, lamb):
    '''poisson function, parameter lamb is the fit parameter'''
    return poisson.pmf(k, lamb)


# fit with curve_fit 
parameters, cov_matrix = curve_fit(fit_function, bin_centers, entries)
print(np.sqrt(cov_matrix))
# plot poisson-deviation with fitted parameter
x_plot = np.arange(0, 70)

plt.plot(x_plot,fit_function(x_plot, *parameters),marker='o', linestyle='dashed',label=f'Fitted Poisson Distribution lambda = {parameters} ')
temps_fin = time.time()
# Calculez la durée totale d'exécution
duree_execution = temps_fin - temps_debut

plt.plot(x_plot,poisson.pmf(x_plot, (T*a)),label=f'poisson with an exact lambda of {T*a} ')
plt.xlim(0, 25)

print(f"Le programme a pris {duree_execution} secondes pour s'exécuter.")
plt.xlabel('Number of clicks')
plt.ylabel('Iterations of clicks / histories')
plt.legend()
plt.show()
