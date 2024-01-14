import numpy as np
import matplotlib.pyplot as plt

t = np.random.randint(2, size=1000) - (1/2) 
x = [sum(t[:i+1]) for i in range(len(t))]

print (x)

plt.plot(x)
plt.legend()
plt.xlabel("$N(steps)$")
plt.ylabel("$x$")
plt.title("1 D")
plt.grid(True)
plt.show()