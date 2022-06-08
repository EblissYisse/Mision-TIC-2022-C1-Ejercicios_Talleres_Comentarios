# def cuenta_regresiva(numero):
#     # Algoritmo
#     if numero > 0:
#         print(numero)
#         cuenta_regresiva(numero - 1)
#     else:
#         print("Boooooooom!")

# cuenta_regresiva(10)

# Factorial
# Definición
# factorial(0) = 1
# factorial(n) = n * factorial(n - 1)

# Solución
# def factorial(n):
#     # Validar
#     if n < 0:
#         return "Número erróneo"
#     # Algoritmo
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))
# Fibonacci
# Definición
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

#Solución
def fibonacci(n):
    # Validar
    if n < 0:
        return "Número erróneo"
    # Algoritmo
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(100))