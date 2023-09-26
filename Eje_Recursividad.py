"""Ejercicio de Recursividad Analisis y diseño de algoritmos Fibonacci & Factorial"""

def fibonacci_R(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_R(n-1) + fibonacci_R(n-2);

def factorial_R(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * factorial_R(n-1);

S2 = []
r = int(input("Hasta donde desea calcular las series: "))
S1 = factorial_R(r)
S2 = fibonacci_R(r)
print(f"El factorial de {r} es: {S1}")
print(f"La serie fibonacci de {r} es: {S2}")