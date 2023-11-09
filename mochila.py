import time
import matplotlib.pyplot as plt

def mochila(objetos, capacidad):
    objetos.sort(key=lambda x: x[0]/x[1], reverse=True)

    total = 0.0
    mochila = []

    for valor, peso in objetos:
        if capacidad >= peso:
            mochila.append((valor, peso))
            total += valor
            capacidad -= peso
        else:
            fracc = capacidad / peso
            mochila.append((valor * fracc, peso * fracc))
            total += valor * fracc
            break

    return total, mochila

if __name__ == '__main':
    tiempos = []
    tamanos = list(range(1, 1001, 50))  # Tamaños de entrada (1 a 1000 en incrementos de 50)

    for n in tamanos:
        objetos = [(i, i) for i in range(1, n + 1)]
        capacidad = n

        start_time = time.time()
        total_valores, elementos = mochila(objetos, capacidad)
        elapsed_time = time.time() - start_time

        tiempos.append(elapsed_time)

    plt.plot(tamanos, tiempos, marker=f'O{n}')
    plt.xlabel(f'Tamaño de la entrada ({n})')
    plt.ylabel(f'Tiempo de ejecución ({tiempos})')
    plt.title('Tiempo de ejecución & Tamaño de entrada')
    plt.grid(True)
    plt.show()
