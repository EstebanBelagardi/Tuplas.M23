#Ejercicios 4 Tuplas

tupla_numeros = ()
indice = 0

tupla_n = (1,2,3,4,5,6,7,8,9,10)
 
indice = int(input("Ingrese un indice: "))
 
if indice >= 0 and indice < len(tupla_n):
    print(tupla_n[indice]) #si el usuario ingresa 5 se imprime la posicion 5 que en la tupla es el numero 6
else:
    print("Indice no valido")