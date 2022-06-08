#Funciones de orden superior: cuando se une con otras funciones
# como funciona el map
#el map hara el proceso de iterracion y lo que diga la funcion

def doblar(numero):
    return numero*2

numero = [2, 3, 5, 7, 20, 50]

print(list(map(doblar, numero)))


#lambda :funcion anonima
#se vuelve funcion de orden superior cuando se junta con un def y dos lambda, si es solo lambda es solo una funcion
#realiza lo del map, simplifica el codigo, pero sigue siendi una funcion 

numero = [2, 3, 5, 7, 20, 50]

print(list(map(lambda x: x*2, numero)))

#ejemplo
#indic, indice o la posicion, lambda solo multiplica en lista 
#lo que tiene igual posicionamiento 
#Cuantas variables puede aceptar lambda = cualquiera 
#y las varibles se pueden llamar como sea
a = [1, 2 , 3, 4, 5]
b = [6,7,8,9,10]

print(list(map(lambda x,y : x*y, a,b)))

#x y son variables locales, a y b es a lo que va a remplazar

#Reduce = Funcion que permite pasar argumentos a una lista de elementos