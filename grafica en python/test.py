import matplotlib.pyplot as plt
import math
import numpy as n
# log(n)
fig, ax = plt.subplots()
ax.set_xlim([0, 500])
ax.set_ylim([0, 500])
for i in range(1,100):
    aux = float(i)
    ax.scatter(aux, math.log(aux));
# n log(n)
for i in range(1,100):
    aux = float(i)
    ax.scatter(aux, aux * math.log(aux));
# Lineal
for i in range(1,100):
    aux = float(i)
    ax.scatter(aux, aux);
# constante
for i in range(1,100):
    aux = float(i)
    ax.scatter(aux, 1);
# cuadratica
for i in range(1,100):
    aux = float(i)
    ax.scatter(aux, aux**2);
# exponencial
for i in range(1,100):
    aux = float(i)
    ax.scatter(aux, 2**aux);
plt.savefig('grafica log.png')
plt.show()