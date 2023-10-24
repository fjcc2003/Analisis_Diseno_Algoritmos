def heap_sort(arreglo, n, i):
    maximo = i
    izquierdo = 2 * i + 1
    derecho = 2 * i + 2

    if izquierdo < n and arreglo[izquierdo] > arreglo[maximo]:
        maximo = izquierdo

    if derecho < n and arreglo[derecho] > arreglo[maximo]:
        maximo = derecho

    if maximo != i:
        arreglo[i], arreglo[maximo] = arreglo[maximo], arreglo[i]
        heap_sort(arreglo, n, maximo)


def heap_maximo(arreglo):
    n = len(arreglo)
    #Construcción del Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heap_sort(arreglo, n, i)
    #Extracción ordenada de elementos
    for i in range(n - 1, 0, -1):
        arreglo[0], arreglo[i] = arreglo[i], arreglo[0]
        heap_sort(arreglo, i, 0)


R = int(input("Cuantos elementos desea ordenar: "))
X = []

for i in range(R):
    numero = int(input(f"Ingrese el número {i}: "))
    X.append(numero)

heap_maximo(X)
print(X)
