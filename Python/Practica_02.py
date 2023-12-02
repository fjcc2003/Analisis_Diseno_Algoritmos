import heapq  # libreria para la cola de prioridad
import time
import os

"""
Francisco Javier Calderon Corrales 3CM1
Analisis y diseño de algoritmos
Saludos xd xd
"""


class Grafos:
    def __init__(self):  # inicializan los atributos, en este caso vertices es un diccionario
        self.vertices = ({})  # Las claves son el nombre del vertice y los valores tuplas de destino y peso

    def add_vertex(self, vertex):
        if (vertex not in self.vertices):  # se verifica si el grafo ya ha sido introducido
            self.vertices[vertex] = ([])  # agrega el vertice igualando a una lista vacia para introducir las tuplas

    def add_edge(self, start, end, weight):  # agrega una arista, recibe el nodo de origen, el nodo de destino y el peso que tendra la arista
        self.vertices[start].append((end, weight))  # se le agrega al nodo de inicio la tupla de destino y peso


def dijkstra(grafo, start_vertex):  # algoritmo de dijkstra
    """
    inicializo el diccionario de distancia, inicializo todas las distancia a todos los nodos
    como infinito menos el nodo de inicio esa distancia siempre sera 0
    """
    distances = {vertex: float("infinity") for vertex in grafo.vertices}
    distances[start_vertex] = 0
    """
    declaro la variable para la cola de prioridad como monticulo binario (heap)
    para seleccionar los vertices conforme a las distancias actuales
    """
    priority_queue = [(0, start_vertex)]
    """
    se inicia el ciclo mientras que la cola de prioridad no este vacia
    en cada iteracion se toma el vertice con la distancia minima
    """
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue
        """
        Uso un ciclo for para los vertices vecinos del vertice actual
        y se actualiza la distancia minima
        """
        for neighbor, weight in grafo.vertices[current_vertex]:
            distance = current_distance + weight
            # los vecinos actualizados se añaden a al cola de prioridad
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    # Por ultimo se retornan las distancias (diccionario) que tienen las distancias minimas
    return distances


def measure_time(func, *args):  # funcion para medir el tiempo de execucion
    start_time = time.time()
    result = func(*args)  # se ejecuta el algoritmo de dijkstra
    end_time = time.time()
    execution_time = end_time - start_time
    return (result, execution_time)  # retorna las distancias minimas y el tiempo de ejecucion


# Crear un grafo de ejemplo
#grafo = Grafos()
# Menu
"""while op != 9:
    os.system("cls")
    start_vertex = "no seleccionado"
    print(grafo.vertices, f" Vertice de inicio {start_vertex}")
    op = int(input("1) ingresar vertice\n2) ingresar aristas\n3) seleccionar vertice de inicio\n4) iniciar Dijkstra\n9) Salir\nSelecciona una opcion: "))
    if op == 1:
        grafo.add_vertex(input("ingrese la letra del vertice: "))
    elif op == 2:
        grafo.add_edge(
            input("ingrese el vertice de origen: "),
            input("ingrese el vertice de destino: "),
            input("ingrese el peso de la arista: "),
        )
    elif op == 3:
        start_vertex = input("ingrese el vertice de inicio: ")
    elif op == 4:
        result, execution_time = measure_time(dijkstra, grafo, start_vertex)
        print(f"Caminos mínimos desde {start_vertex}: {result}")
        print(f"Tiempo de ejecución: {execution_time} segundos")
    elif op == 9:
        print("Gracias por usar el programa!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("Seleccione una opcion valida")"""
#CASO 1
# Grafo de ejemplo
grafo = Grafos()
grafo.add_vertex("A")
grafo.add_vertex("B")
grafo.add_vertex("C")
grafo.add_edge("A", "B", 3)
grafo.add_edge("A", "C", 5)
grafo.add_edge("B", "C", 2)

# Algoritmo de Dijkstra
start_vertex = "A"
result, execution_time = measure_time(dijkstra, grafo, start_vertex)

# Resultado e interpretación
print(f"Caminos mínimos desde {start_vertex}: {result}")
print(f"Tiempo de ejecución: {execution_time} segundos")

#CASO 2
# Grafo de ejemplo
grafo2 = Grafos()
grafo2.add_vertex("A")
grafo2.add_vertex("B")
grafo2.add_vertex("C")
grafo2.add_vertex("D")
grafo2.add_edge("A", "B", 2)
grafo2.add_edge("C", "D", 4)

# Algoritmo de Dijkstra
start_vertex = "A"
result, execution_time = measure_time(dijkstra, grafo2, start_vertex)

# Resultado e interpretación
print(f"Caminos mínimos desde {start_vertex}: {result}")
print(f"Tiempo de ejecución: {execution_time} segundos")

#CASO 3
# Grafo de ejemplo
grafo3 = Grafos()
grafo3.add_vertex("A")
grafo3.add_vertex("B")
grafo3.add_vertex("C")
grafo3.add_edge("A", "B", 3)
grafo3.add_edge("B", "C", -2)
grafo3.add_edge("C", "A", 1)

# Algoritmo de Dijkstra
start_vertex = "A"
result, execution_time = measure_time(dijkstra, grafo3, start_vertex)

# Resultado e interpretación
print(f"Caminos mínimos desde {start_vertex}: {result}")
print(f"Tiempo de ejecución: {execution_time} segundos")

#CASO 4
# Grafo de ejemplo grande
grafo4 = Grafos()
for i in range(1, 1001):
    grafo4.add_vertex(str(i))
    if i < 1000:
        grafo.add_edge(str(i), str(i + 1), 1)

# Algoritmo de Dijkstra
start_vertex = "1"
result, execution_time = measure_time(dijkstra, grafo4, start_vertex)

# Resultado e interpretación
print(f"Caminos mínimos desde {start_vertex}: {result}")
print(f"Tiempo de ejecución: {execution_time} segundos")

#CASO 5
# Grafo de ejemplo
grafo5 = Grafos()
grafo5.add_vertex("A")
grafo5.add_vertex("B")
grafo5.add_vertex("C")
grafo5.add_edge("A", "B", 3)
grafo5.add_edge("A", "C", 5)
grafo5.add_edge("B", "C", 2)
grafo5.add_edge("B", "A", 1)

# Algoritmo de Dijkstra
start_vertex = "A"
result, execution_time = measure_time(dijkstra, grafo5, start_vertex)

# Resultado e interpretación
print(f"Caminos mínimos desde {start_vertex}: {result}")
print(f"Tiempo de ejecución: {execution_time} segundos")
