import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import poisson
import time



#Take the necessary tables
choix = []
liste_fusionnee = []

# just for executions time
temps_debut = time.time()

# matrix 5*10^4
r = np.arange(0., 8., 1) #table of cliks with an expecting of 8 clicks per average
tab = []

for i in range (10000): #multiply the table of clicks as much as there is of historys
    tab += [r]

for sous_liste in tab: #put everythong in only one list
    liste_fusionnee.extend(sous_liste)

# parameter 
taux = 8

#generate values with poisson distribution 
valeurs_poisson = np.random.poisson(lam=taux, size=len(liste_fusionnee))

temps_fin = time.time()


# for plots
bins = np.arange(len(set(valeurs_poisson))) - 0.5
entries, bin_edges, patches = plt.hist(valeurs_poisson, bins=bins,color='lightgreen', density=True, label='Simulated Data')

bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

#Fitting curve
def fit_function(k, lamb):
    return poisson.pmf(k, lamb)


parameters, cov_matrix = curve_fit(fit_function, bin_centers, entries, p0=[taux])
print(parameters)
#plot
plt.plot(bin_centers,poisson.pmf(bin_centers, taux),color="blue",label=f'theoritical poisson with lambda = {taux}')

plt.plot(bin_centers, fit_function(bin_centers, parameters),"--",marker='.',color='red' , label=f'Fitted Poisson Distribution lambda = {parameters} ' )
plt.legend()
plt.xlim(0,25)
plt.xlabel('Number of customers served')
plt.ylabel('customers served / rushes')
plt.title("Histogram of customers served over 10 000 rushes")
plt.legend()

plt.show()



#just for execution time
duree_execution = temps_fin - temps_debut
print(f"Le programme a pris {duree_execution} secondes pour s'exécuter.")
