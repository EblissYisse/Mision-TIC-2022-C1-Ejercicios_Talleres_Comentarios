Ejercicio1 Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

num = (input("Digite un numero entero de dos digitos: "))


def num_par (num = str):
    digito1 = int (num[0])
    digito2 = int (num[1])
    
    if digito1 % 2 == 0:
        print ("El primer digito es par")
        if digito2 % 2 == 0:
            print ("El segundo digito es par")
        else:
            print ("El segundo digito no es par")
    else:
        print ("El primer digito no es par")

print (num_par (num))

Ejercicio2 A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. 
Si la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las horas extras.
 Calcular el salario del trabajador dadas las horas trabajadas y la tarifa ingresadas por el usuario.

tarifa = float(input("Ingrese la tarifa: "))
Hora = int(input("Ingrese el numero de horas trabajadas: "))
Hora_Extra = int(input("Ingrese el numero de horas extras trabajadas: "))
def salario (tarifa = float, Hora = int, Hora_Extra = int):
    if Hora > 40:
        hora_dia_normal = Hora - Hora_Extra
        Hora_dia = tarifa * hora_dia_normal
        incremento_tarifa = tarifa / 2
        tarifa_horas_extras = tarifa + incremento_tarifa
        Pago_HE = Hora_Extra * tarifa_horas_extras
        Dia = Hora_dia + Pago_HE
        print (f"El salario es de: {Dia}")
    else:
        Dia = Hora * tarifa
        print (f"El salario es de: {Dia}")
        
print(salario(tarifa, Hora, Hora_Extra))
print(40 * 5000 + 5 * 7500)

Ejercicio3
Hacer un algoritmo que calcule el total a pagar por la compra de camisas. 
Si se compran tres camisas o más se aplica un descuento del 20% sobre el 
total de la compra y si son menos de tres camisas un descuento del 10%

camisa = int (input("Cuantas Camisas compraste: "))
Costo_camisa = float (input("Cuanto vale cada camisa: "))
def totalPago (camisa = int):
    if camisa >= 3:
       pago = camisa * Costo_camisa 
       porcentage_20 = ((pago * 20) / 100 )
       totalCompra = pago - porcentage_20
       print(f"El total a pagar por la compra es {totalCompra}")
    else: 
       pago = camisa * Costo_camisa
       porcentage_10 = ((pago * 10) / 100 )
       totalCompra = pago - porcentage_10
       print(f"El total a pagar por la compra es {totalCompra} ")

print(totalPago(camisa))

Ejercicio 4
Escribir un programa que pregunte el nombre del usuario en la consola y 
un número entero e imprima por pantalla en líneas distintas el nombre del 
usuario tantas veces como el número introducido
