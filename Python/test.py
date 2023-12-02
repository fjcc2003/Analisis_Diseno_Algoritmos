import heapq  # Librería para la cola de prioridad
import time
import os

class Grafo:
    def _init_(self):
        # Inicializan los atributos, en este caso, vertices es un diccionario
        self.vertices = ({})  # Las claves son el nombre del vértice y los valores son listas de tuplas (destino, peso)

    def add_vertex(self, vertex):
        # Se verifica si el vértice ya ha sido introducido
        if vertex not in self.vertices:
            # Agrega el vértice igualando a una lista vacía para introducir las tuplas
            self.vertices[vertex] = ([])

    def add_edge(self, start, end, weight):
        # Agrega una arista, recibe el nodo de origen, el nodo de destino y el peso que tendrá la arista
        self.vertices[start].append((end, weight))  # Se agrega al nodo de inicio la tupla de destino y peso

def dijkstra(grafo, start_vertex):
    """
    Inicializo el diccionario de distancia, inicializo todas las distancias a todos los nodos
    como infinito menos el nodo de inicio cuya distancia siempre será 0
    """
    distances = {vertex: float("infinity") for vertex in grafo.vertices}
    distances[start_vertex] = 0

    """
    Declaro la variable para la cola de prioridad como un montículo binario (heap)
    para seleccionar los vértices conforme a las distancias actuales
    """
    priority_queue = [(0, start_vertex)]

    """
    Se inicia el ciclo mientras que la cola de prioridad no esté vacía
    en cada iteración se toma el vértice con la distancia mínima
    """
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        """
        Uso un ciclo for para los vértices vecinos del vértice actual
        y se actualiza la distancia mínima
        """
        for neighbor, weight in grafo.vertices[current_vertex]:
            distance = current_distance + weight
            # Los vecinos actualizados se añaden a la cola de prioridad
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Por último, se retornan las distancias (diccionario) que tienen las distancias mínimas
    return distances

def measure_time(func, *args):
    # Función para medir el tiempo de ejecución
    start_time = time.time()
    result = func(*args)  # Se ejecuta el algoritmo de Dijkstra
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time  # Retorna las distancias mínimas y el tiempo de ejecución

# Crear un grafo de ejemplo
grafo = Grafo()

# Menú
op = 0
start_vertex = "no seleccionado"

while op != 9:
    os.system("cls")
    print(grafo.vertices, f" Vertice de inicio {start_vertex}")
    op = int(input("1) Ingresar vértice\n2) Ingresar aristas\n3) Seleccionar vértice de inicio\n4) Iniciar Dijkstra\n9) Salir\nSelecciona una opción: "))
    
    if op == 1:
        grafo.add_vertex(input("Ingrese la letra del vértice: "))
    elif op == 2:
        grafo.add_edge(
            input("Ingrese el vértice de origen: "),
            input("Ingrese el vértice de destino: "),
            input("Ingrese el peso de la arista: "),
        )
    elif op == 3:
        start_vertex = input("Ingrese el vértice de inicio: ")
    elif op == 4:
        result, execution_time = measure_time(dijkstra, grafo, start_vertex)
        print(f"Caminos mínimos desde {start_vertex}: {result}")
        print(f"Tiempo de ejecución: {execution_time} segundos")
    elif op == 9:
        print("¡Gracias por usar el programa!")
    else:
        print("Seleccione una opción válida")