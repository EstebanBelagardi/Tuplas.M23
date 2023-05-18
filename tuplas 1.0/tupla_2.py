# Ejercicio 2 Tupla

num = 0
con = 0
tupla_n = ()

tupla_n = (1,6,1,2,3,1,1,7,5,8,5,3,8,3,6,1,6,6,6,6,8,8,4,9,9)

num = int(input("Ingrese un numero: "))

if num > 0 and num < 10:
    for i in tupla_n:
        if num ==  i:
            con = con + 1
    print("El numero "+ str(num) + " se repite "+ str(con) + " cantidad de veces")
else:
    print("El numero no se encuentra en la secuencia")