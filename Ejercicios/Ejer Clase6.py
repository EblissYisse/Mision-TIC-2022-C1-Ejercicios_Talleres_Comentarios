ejercicio5
numero = float(input ("Ingrese un numero: "))

def rango(numero: float):
   
   if numero > 3.5 and numero <= 7.8:
      print(f"El numero {numero} esta en el rango abierto - cerrado (3.5, 7.8]\n")
   else:
      print("El numero no esta en el rango abierto - cerrado (3.5, 7.8] ")
      return rango

print(rango(numero))
      
Ejercicio6- Diseñe un algoritmo que determine si un número real (x) se encuentra dentro de uno 
de los siguientes rangos: (3.5, 7.8], [9.3, 4.5) y [23.4, 45.3].

num = float (input ("Ingrese un numero: "))

def rango(num: float):

 if num > 3.5 and num <= 7.8:
   print(f"el numero {num} estan en el rango (3.5, 7.8] ")

 if num > 4.5 and num <= 9.3:
   print(f"el numero {num} estan en el rango (4.5, 9.3] ")
 else: 
      
      if num >= 23.4 and num <= 45.3:
         print(f"el numero {num} estan en el rango [23.4, 45.3] ")
      else:
        print(f"el numero {num} no esta en ninguno de los rangos ")
   
print(rango(num))


ejercico7
caracter = input ("Ingrese el caracter especial: ")


if caracter == 'a' or caracter == 'A':  #no hay necesidad de convertilo a str, porque input devuelve una cadena
   print("Android")
else : 
   if caracter == 'i' or caracter == 'I':
      print("IOS")
   else: 
      print("Opción inválida")
   


nota = float (input ("Ingrese nota del estudiante:") )
 
def nota_estudiante (nota: float):
   if nota < 3.0 and nota >= 0:
      print(" Insuficiente ")
   else:
      if nota >= 3.0 and nota <= 3.5:
         print(" Aceptable ")
      else:
         if nota >= 3.6 and nota <= 4.0:
            print(" Sobresaliente ")
         else:
            if nota >= 4.1 and nota <= 5.0:
               print(" Excelente ")
            else:
               print(" Nota ingresada es invalida ")

print (nota_estudiante(nota))

Ejercicio 9 Diseñe un algoritmo que determine mayor número entre cuatro posibles números.

n1 = float (input ("Ingrese primer numero: "))
n2 = float (input ("Ingrese segundo numero: "))
n3 = float (input ("Ingrese tercer numero: "))
n4 = float (input ("Ingrese cuarto numero: ")) 

def num_mayor (n1, n2, n3, n4: float):
   
      if n2 < n1 > n3 and n1 > n4:
        print(f"el numero {n1} es mayor que {n2} , {n3} y {n4} ")
      elif n1 < n2 > n3 and n2 > n4:
        print(f"el numero {n2} es mayor que {n1} , {n3} y {n4} ")
      elif n1 < n3 > n2 and n3 > n4:
        print(f"el numero {n3} es mayor que {n1} , {n2} y {n4} ")
      elif n1 < n4 > n3 and n4 > n2:
        print(f"el numero {n4} es mayor que {n1} , {n3} y {n2} ")
   
print (num_mayor(n1,n2,n3,n4))

Ejercicio 10



estrato = int (input("Ingrese su estrato: "))
consumo = float (input("Ingrese cual fue el consumo del mes: "))

def metro2 (estrato = int , consumo = float):
   if estrato < 1 or estrato > 6:
      print ("El estrato debe estar entre 1 y 6")
   if consumo < 0:
      print ("El consumo debe ser igual o mayor a cero")

   tarifas = {

      1: {"Cargo Fijo" : 2500, "Metro3 Consumido" : 2200, "Basura y Alcantarillado" : 5500},
      2: {"Cargo Fijo" : 2800, "Metro3 Consumido" : 2350, "Basura y Alcantarillado" : 6200},
      3: {"Cargo Fijo" : 3000, "Metro3 Consumido" : 2600, "Basura y Alcantarillado" : 7400},
      4: {"Cargo Fijo" : 3300, "Metro3 Consumido" : 3400, "Basura y Alcantarillado" : 8600},
      5: {"Cargo Fijo" : 3700, "Metro3 Consumido" : 3900, "Basura y Alcantarillado" : 9700},
      6: {"Cargo Fijo" : 4400, "Metro3 Consumido" : 4800, "Basura y Alcantarillado" : 11000}    
   }
   
   valor_factura = tarifas[estrato]["Cargo Fijo"]
   valor_factura += consumo * tarifas[estrato]["Metro3 Consumido"]
   valor_factura += tarifas[estrato]["Basura y Alcantarillado"]
   

   return valor_factura
   
print(metro2(estrato, consumo))

ejercicio 11

Sexo = (input("¿Cual es su sexo?. \nNota: Digite M si es mujer o H si es hombre: "))
Estatura = float (input("Por favor digite su estatura: "))
Edad = int (input("Por favor digite su edad: "))

def apto_o_apta (Sexo = str , Estatura = float, Edad = int):
    if Sexo == str ("M") or Sexo == str ("m"):
       if Estatura > 1.60 and Edad >= 20 and Edad <= 25:
         print("Es apta para entrar al ejercito")
       else: 
         print("No es apta para entrar al ejercito") 
    else:
        if Estatura > 1.65 and Edad >= 18 and Edad <= 24:
         print("Es apto para entrar al ejercito")
        else: 
         print("No es apto para entrar al ejercito") 

print (apto_o_apta(Sexo, Estatura, Edad))


#Ejercicio3
#una funcion tiene 
#Datos de entrada
#Proceso
#salida
#intento 1 con funciones
def EDAD_NOMBRE (EDAD : int  , NOMBRE : str)

if EDAD < 18:

    Mensaje : "por lo tanto es menor de edad"
else
    
    Mensaje :"por lo tanto es mayor de edad"
    
return f"La edad de: {NOMBRE} es {EDAD} {Mensaje}"

#Prueba del algoritmo
EDAD = int (input("Ingrese su edad : "))
NOMBRE = str (input("Ingrese su nombre : "))

print(EDAD(EDAD))

#intento dos con solo condicionales

NOMBRE = str(input("Ingrese su nombre:"))
EDAD = int(input("Ingrese su edad: "))

if EDAD < 18:
    print(f"El usuario ingresado de nombre {NOMBRE} tiene {EDAD} años, por lo tanto es menor de edad.")
else:
    print(f"El usuario ingresado de nombre {NOMBRE} tiene {EDAD} años, por lo tanto es mayor de edad.")
    
   
   #Ejercicio 4

Num = int(input ("Ingrese un numero: "))
resto = Num % 2

if resto == 0: 
    
    print(f"El numero ingresado {Num} es par")
else:
    print(f"El numero ingresado {Num} no es par")
