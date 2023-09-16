"""
Practica 01: Analisis de Casos
Francisco Javier Calderon Corrales - 2022670255 - 3CM1
"""
import time
import random
import os
op = str  # Variable para seleccionar las opciones del menu
ordenamiento = "\033[91mSeleccione un tipo de ordenamiento\033[0m"  # Variable para verbose para claridad para el usuario
array = [] # se declara el arreglo que se usara para ordenar
aux = int(0) # variable auxiliar para definir el tamaño del arreglo


def burbuja(arr): # Ordenamiento por burbuja
    n = len(arr)
    inicio = time.time() # se guarda el tiempo antes de que se inicie el algoritmo de burbuja
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambia los elementos si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    fin = time.time() # se guarda el tiempo despues de terminado el algoritmo
    print(f"el arreglo ordenado es: {arr}")
    print(f"\033[93mTiempo de Ejecucion: {fin - inicio} Segundos\033[0m") # se imprime el tiempo de ejecucion
    os.system("pause")

def burbuja_optimizado(arr):
    n = len(arr)
    inicio = time.time()
    for i in range(n - 1):
        intercambio = False 
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambia los elementos si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio = True  # Marca que se ha realizado un intercambio
        if not intercambio: # si no hubo intercambio es porque el arreglo ya esta ordenado por ende se termina el ciclo
            break
    fin = time.time()
    print(f"el arreglo ordenado es: {arr}")
    print(f"\033[93mTiempo de Ejecucion: {fin - inicio} Segundos\033[0m")
    os.system("pause")

while op != "exit" or op != "EXIT":  # ciclo para controlar el menu
    os.system("cls")
    print(
        f"Ordenamiento: {ordenamiento}\nMENU\nA) Ordenamiento Burbuja\nB) Ordenamiento Burbuja Optimizada\nC) introducir Array\nD) Iniciar el Ordenamiento\n-> Para salir escriba exit"
    )  # Menu
    op = input("Seleccione una opcion: ")
    if op == "A" or op == "a":
        ordenamiento = "\033[92mOrdenamiento Burbuja\033[0m"
    elif op == "B" or op == "b":
        ordenamiento = "\033[92mOrdenamiento Burbuja Optimizada\033[0m"
    elif op == "C" or op == "c":
        if len(array) == 0:
            aux = int(input("ingrese el Tamaño del array: "))
            print("1) llenar array aleatorio\n2) Mejor caso\n3) Peor caso\n4) llenar manualmente")
            op = input("Seleccione una opcion: ")
            if op == "1":
                for i in range(1, aux):
                    array.append(random.randint(1, aux))
            elif op == "2":
                for i in range(1, aux):
                    array.append(i)
            elif op == "3":
                for i in range(aux, 1, -1):
                    array.append(i)
            elif op == "4":
                for i in range(1, aux):
                    array.append(input(f"ingrese el numero [{i}]: "))
            print(f"el array es: {array}")
            os.system("pause")
        else:
            op = input("ya hay un array existente, desea eliminarlo?(y/n): ")
            if op == "y" or op == "Y":
                del array[:]
            else:
                continue
    elif op == "D" or op == "d":
        if len(array) == 0:
            print("el array esta vacio, primero llene el array")
            os.system("pause")
        elif ordenamiento == "\u001b[91mSeleccione un tipo de ordenamiento\u001b[0m":
            print("Primero seleccione un tipo de ordenamiento")
            os.system("pause")
        elif ordenamiento == "\u001b[92mOrdenamiento Burbuja\u001b[0m":
            burbuja(array)
        elif ordenamiento == "\u001b[92mOrdenamiento Burbuja Optimizada\u001b[0m":
            burbuja_optimizado(array)
    elif op == "exit" or op == "EXIT": #condicion para cerrar el programa
        break;