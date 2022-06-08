nombres = ["Ana", "Bernardo"]
edades = [22.0, 21]
lista = [nombres, edades]

for <elemento> in <lista>:
    <sentencias usando elemento>

for elemento in lista:
    tam = len(elemento)
    print(elemento, tam, sep=" -> ")
    if tam > 0:
        for dato in elemento:
            if isinstance(dato, int) or isinstance(dato, float):
                print(dato, "no es una colección")
            else:
                print(dato, len(dato), sep=" -> ")
print(len(lista))
print(len(lista[0]))
print(len(lista[0][1]))

#la funcion insisnstance ayuda a saber o a validar cual es el tipo de datos
#funcion append agregan al final
versiones.append(7)
print(versiones)

#Contar elementos repetidos en la lista
print("5 ->", versiones.count(5))
print("6 ->", versiones.count(6))

#Extender la lista con otra secuencia (colección)
versiones.extend([4, 8, 9])
print(versiones)

versiones.extend(range(5,7))
print(versiones)

#Encontrar la posición de un elemento
print(versiones.index(4))

#donde esta el 4 despues de la posicion 3
print(versiones.index(4, 3))
#donde esta eñ 4 despues de la posicion 8
print(versiones.index(4, 8))

#Insertar un elemento en una posición en la lista
print(versiones)
#en la posicion 2 de la lista insertar el 3.1
versiones.insert(2, 3.7)
print(versiones)

#Eliminar el último elemento de la lista

ultimo = versiones.pop()
print(f"Extrae {ultimo} y queda {versiones}")

elemento = versiones.pop(5)
print(f"Extrae {elemento} de la posición 5 y queda {versiones}")


#Eliminar un elemento dentro de la lista (enviando el elemento)
versiones.remove(2.5)
print(versiones)

#Invertir una lista
print(versiones)
versiones.reverse()
print(versiones)

#Ordenar la la lista
#manera accendente

versiones.sort()
print(versiones)

#manera descendiente
versiones.sort(reverse=True)
print(versiones) 

#Borrar el contenido de una lista
versiones.clear() 
print(versiones)

#Eliminar una variable de python (y la lista tambien)
del versiones
print(versiones)

#Todos los métodos y atributos de las listas
print(dir(list()))

#Funciones útiles para crear listas
mensaje = "Hola, como estas tu?"
lista = list(mensaje)
print(lista)
lista = mensaje.split()
print(lista)