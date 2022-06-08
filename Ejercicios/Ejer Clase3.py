num_1 = input("Ingrese el primer número:")
num_2 = input("Ingrese el segundo número:")

print(type(num_1), type(num_2))

num_1 = int(num_1)
num_2 = int(num_2)

print(type(num_1), type(num_2))

print(num_1, "*", num_2, "=", num_1 * num_2)

#INTENTO DE FUNCIONES
def totalpeces(peces_rojos, peces_azules):
    Total_de_peces = (peces_rojos + peces_azules)
    return Total_de_peces


#pidiendo los datos al usuario

Peces_rojos =  int (input("Ingrese la cantidad de peces rojos que estan en el acuario: "))
Peces_azules =  int (input("Ingrese la cantidad de peces azules que estan en el acuario: "))

a = ejer3.totalpeces(Peces_rojos, Peces_azules)
print(a)

#poniendo los datos
#a = ejer3.totalpeces(10, 20)

#print(a)
