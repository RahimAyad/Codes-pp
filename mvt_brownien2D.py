import numpy as np
import matplotlib.pyplot as plt
N = 1000
t1 = np.random.randint(2, size=N) - (1/2) 
t2 = np.random.randint(2, size=N) - (1/2) 
x = [sum(t1[:i+1]) for i in range(len(t1))]
y = [sum(t2[:i+1]) for i in range(len(t2))]


plt.plot(x,y)
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("2 D")
plt.grid(True)
plt.show()