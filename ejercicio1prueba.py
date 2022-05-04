#Ejercicio 1 prueba 1

barras = int(input("ingrese cantidad de barras de pan que no son del día: "))

precioi = 3.49

preciof = (precioi * barras)

descuento = ((preciof * 60)/100)

preciot = (preciof - descuento)

print("Valor a pagar por barras de pan que no son del día: ")

print(preciof)

print("el descuento aplicado por pan que no es del día es: ")

print(round(descuento,2))

print("El valor final a pagar es de: ")

print(round(preciot,2))
