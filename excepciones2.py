def divide():
	try:
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("La división es: "+ str(op1/op2))
	except ValueError:
		print("El valor introducido es erróneo")
	except ZeroDivisionError:
		print("No se puede dividir entre cero")

	finally:
		print("Ca lculo finalizado")

#divide()

import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError("El número no puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("El programa ha terminado")