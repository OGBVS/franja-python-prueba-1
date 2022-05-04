#ejercicio 3 prueba 1

print("*******CONVERSOR DE MONEDAS*********")
print("A)Para peso Chileno marque 1")
print("B)Para peso Argentino marque 2")
print("C)Para peso Mexicano marque 3")

pais = int(input("Ingrese pais de moneda a transformar: "))

if pais == 1:
    montochile = float(input("Ingrese monto a convertir: "))
    totalchile = (montochile/855)
    print("El monto a convertir es de: ")
    print(montochile)
    print("El monto convertido, en dolares es: ")
    print(round(totalchile,2))
elif pais == 2:
    montoargentina = float(input("Ingrese monto a convertir: "))
    totalargentina = (montoargentina/115)
    print("El monto a convertir es de: ")
    print(montoargentina)
    print("El monto convertido en dolares es: ")
    print(round(totalargentina,2))
else:
    montomexico = float(input("Ingrese monto a convertir: "))
    totalmexico = (montomexico/20)
    print("El monto a convertir es de: ")
    print(montomexico)
    print("El monto convertido, en dolares es: ")
    print(round(totalmexico,2))
