#Ejercicio 1 tupla 

marca = ""
precio_max = 0

lista_tuplas = [("fiat", 10000, 5, "uno"), ("ford", 12000, 3, "fiesta"), ("fiat", 9000, 4, "siena")]

precio_max = int(input("Ingrese precio maximo: "))
marca = (input("Ingrese marca especifica: "))

lista_final = []



for t in lista_tuplas:
    if t[1] <= precio_max and t[3] == marca:
        lista_final.append(t)

print(lista_final)



