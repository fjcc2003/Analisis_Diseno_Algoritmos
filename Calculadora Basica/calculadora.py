"""
________________________________________________________________________________
Calculadora basica en python para la materia de analisis y diseño de algoritmos
Hecho por: Francisco Javier Calderon Corrales
________________________________________________________________________________
"""
a, b, c = 0.0, 0.0, 0.0
op = "T"  # variable que controla el menu
while op != "E" or op != "e":  # Cambia "or" a "and" aquí
    print("MENU\nA) SUMA\nB) RESTA\nC) DIVISION\nD) MULTIPLICACION\nE) SALIR")
    op = input("Seleccione una opcion => ")
    if op == "A" or op == "a":
        a = float(input("Ingrese el primer numero a sumar: "))  # Usa float para convertir a números flotantes
        b = float(input("Ingrese el segundo numero a sumar: "))
        c = a + b
        print(f"El resultado de la suma es: {c}")
    elif op == "B" or op == "b":
        a = float(input("Ingrese el primer numero a restar: "))
        b = float(input("Ingrese el segundo numero a restar: "))
        c = a - b
        print(f"El resultado de la resta es: {c}")
    elif op == "C" or op == "c":
        a = float(input("Ingrese el primer numero a dividir: "))
        b = float(input("Ingrese el segundo numero a dividir: "))
        if b != 0:
            c = a / b
            print(f"El resultado de la división es: {c}")
        else:
            print("No se puede dividir entre cero.")
    elif op == "D" or op == "d":
        a = float(input("Ingrese el primer numero a multiplicar: "))
        b = float(input("Ingrese el segundo numero a multiplicar: "))
        c = a * b
        print(f"El resultado de la multiplicación es: {c}")
    elif op == "E" or op == "e":
        print("Gracias por usar el programa")
        break
    else:
        print("Seleccione una opcion valida")
