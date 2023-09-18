import os

def fibonacci(n):
    fibonachi = [0, 1, 1]
    if n <= 3:
        return fibonachi
    else:
        for i in range(3, n+1):
            fibonachi.append(fibonachi[i-1] + fibonachi[i-2])
        return fibonachi
    
def factorial(n):
   if n==0 or n==1:
            r=1
   else:
            r=n*factorial(n-1)
   return r

num = int(input("ingrese hasta donde desea el factorial & fibonacci: "))
print(f"La serie fibonacci hasta {num} es: {fibonacci(num)}")
print(f"El factorial hasta {num} es: {factorial(num)}")