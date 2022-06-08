#se utiliza el # para declarar comentarios

#Tipos de variables 

#Declaramos la variable de tipo entero

var_int = 50

#Podemos declarar otro tipo de variables, puede ser una de tipo float o double
#que son variables de tipo decimal, y la diferencia entre estas es el espacio de la memoria que tiene cada una de ellas
var_pi = 3.1416

#Declaramos otra variable de tipo cadena de texto
#para declarar un texto se utliza un string
var_string = "Grupo_58"

#Variable de tipo Boolean, estas tienen dos estados, falso o verdadero
var_boolean = False

#Variable de tipo diccionario
var_dict = {
    "nombre" : "juliana",
    "apellido" : "Correa",
    "Edad" : " 37"
}

#Podemos modificar el valor de un campo del diccionario, de la siguiente forma

var_dict["nombre"] = "Maria"

#Agregar un campo al diccionario

var_dict["peso"] = 57.5

#Eliminar un campo al diccionario, mediante la funcion pop.()


var_dict.pop("apellido")

#ahora vamos a imprimir las variabes que creamos, mediante print

print("El nombre de la persona es " +  var_dict["nombre"] + " y tiene" + var_dict["Edad"])
print(f"El nombre de la persona es  {var_dict['nombre']} y tiene {var_dict['Edad']}")

#La f es para darle forma y que el programa reconozca las variables

#la comilla " y ' se utilizan para determinar cadena de texto


var = 200 + 300
print(var)
#el siguiente codigo es para mirar que tipo de variable estamos manejando 
print(type(var))

#declaracion de una variable float

var1= 1.75
print(var1)
#castear(volverla un tipo de datos) variable de float a un entero

var1 = int (var1)
print(var1)

#orden de las operaciones

#PEMDAS, es util para recordar
#PEMDAS (parentecis, Exponenciacion, multipicacion y divicion, sumas y restas, las 4 ultimas estan en el 
#mismo orden y se lee de izquierda a derecha

'''
las tres comillas sencillas se utlizan para comentar un codigo

'''
#Como calcular promedio

var1 = 1.0
var2 = 4.5
var3 = 5.5
var4 = 2.5

Promedio = (var1 + var2 + var3 + var4)/4

print("El promedio de esos numeros es: " + str(Promedio))

#la variable round es para redondear el resultado 
print("El promedio de esos numeros es: ", round(Promedio))

#promedio, 2, le da dos decimales al resultado
print("El promedio de esos numeros es: ", round(Promedio,2))



