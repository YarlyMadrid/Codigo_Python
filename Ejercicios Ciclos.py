#TALLER CICLOS 15/02/2020

#Pregunta 3
print("\nEJERCICIO 3\n")
def divisoresExactos(numero):
	divisores=[]
	for i in range(1,numero+1,1):
		if (numero%i==0):
			divisores+=[i]
	print(divisores)

divisoresExactos(8)

#Pregunta 9
print("\nEJERCICIO 9\n")
def terminados6():
	for i in range(25,206):
		if (i%10==6):
			print(i, end="-")

terminados6()

#Pregunta 12
print("\nEJERCICIO 12\n")
def Digito1(numero):
	validacion=False
	if (numero>99)&(numero<1000):
		for i in str(numero):
			if i=="1":
				validacion=True
	return validacion
	print(validacion)

print(Digito1(789))
print(Digito1(715))

#Pregunta 14
print("\nEJERCICIO 14\n")
def Multiplos3():
	contador = 0
	i = 1
	while contador<20:
		if (i%3==0):
			print(i, end="-")
			contador+=1
		i+=1

Multiplos3()

#Pregunta 21
print("\nEJERCICIO 21\n")
def sumaDigitos(numero):
	suma = 0
	for i in str(numero):
		suma = suma + int(i)
	return suma

print(sumaDigitos(9911))

#Pregunta 27
print("\nEJERCICIO 27\n")
def mayorDigitos(numero1,numero2):
	cantidad1 = len(str(numero1))
	cantidad2 = len(str(numero2))
	if(cantidad1>cantidad2):
		print("El número ",numero1," tiene más cantidad de digitos")
	elif(cantidad1<cantidad2):
		print("El número ",numero2," tiene más cantidad de digitos")
	else:
		print("Tienen la misma cantidad de digitos")

mayorDigitos(858,78)
mayorDigitos(74,4545)
mayorDigitos(454,485)

#Pregunta 19
print("\nEJERCICIO 32\n")
def Primo(numero):
	contador = 0
	from math import ceil
	if (numero==1):
		return False
	elif (numero==2):
		return True
	else:
		for i in range(2,ceil(numero/2)+1):
			if (numero%i == 0):
				contador+=1
		if (contador==0):
			return True
		else:
			return False


print(Primo(11))

#Pregunta 32
print("\nEJERCICIO 32\n")

def promedioPrimos():
	conteo = 0; suma = 0
	numero = int(input("Introduzca un numero y pare en cero: "))
	i = 0
	while numero != 0:
		if (Primo(numero)):
			conteo+=1
			suma = suma + numero
		numero = int(input("Introduzca un numero y pare en cero: "))
	promedio = suma/conteo
	return promedio

print(promedioPrimos())


#Pregunta 39
print("\nEJERCICIO 39\n")

def serieFibonacci():
	serie=[0,1]
	ultimo=1; i=1
	while ultimo<10000:
		serie.append((serie[i-1]+serie[i]))
		ultimo=(serie[i-1]+serie[i])
		i+=1
	return serie

print(serieFibonacci())

#Pregunta 43
print("\nEJERCICIO 43\n")

def serieFibonacci2():
	contador=0;i=1;ultimo=1
	serie=[0,1]
	while ultimo<2000:
		serie.append((serie[i-1]+serie[i]))
		ultimo=(serie[i-1]+serie[i])
		if (serie[i]>1000) and (serie[i]<2000):
			contador+=1
		i+=1
	return contador

print(serieFibonacci2())

#Pregunta 48
print("\nEJERCICIO 48\n")

def anidados():
	contador=1
	i=1;j=0

	while (j<=9):
		while (i<=2):
			print(j," ",contador,"\n")
			i=i+1
			j=j+1
		contador=contador+1

anidados()