#ejercicio 2 prueba 1

inversion = float(input("Ingrese monto a invertir: "))

interes = float(input("Ingrese interés porcentual anual: "))

anos = float(input("Ingrese cantidad de años: "))

capital = (inversion * ((interes/100)+1)**anos)

print(round(capital,2))
