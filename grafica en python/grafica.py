import matplotlib.pyplot as plt
import math
import numpy as n
# log(n)
fig, ax = plt.subplots()
for i in range(1,100):
    aux = float(i)
    ax.scatter(aux, y = math.log(aux));
plt.savefig('grafica log.png')
plt.show()
# n log(n)
fig, ax1 = plt.subplots()
for i in range(1,100):
    aux = float(i)
    ax1.scatter(aux, y = aux * math.log(aux));
plt.savefig('grafica nlog.png')
plt.show()
# Lineal
fig, ax2 = plt.subplots() 
for i in range(1,100):
    aux = float(i)
    ax2.scatter(aux, y = aux);
plt.savefig('grafica lineal.png')
plt.show()
# constante
fig, ax3 = plt.subplots()
for i in range(1,100):
    aux = float(i)
    ax3.scatter(aux, y = 1);
plt.savefig('grafica constante.png')
plt.show()
# cuadratica
fig, ax4 = plt.subplots()
for i in range(1,100):
    aux = float(i)
    ax4.scatter(aux, y = aux**2);
plt.savefig('grafica cuadratica.png')
plt.show()
# exponencial
fig, ax5 = plt.subplots()
for i in range(1,100):
    aux = float(i)
    ax5.scatter(aux, y = 2**aux);
plt.savefig('grafica exponencial.png')
plt.show()