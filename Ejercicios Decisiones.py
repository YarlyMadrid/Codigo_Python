print("EJERCICIO 1\n")

def ejercicio1(numero):
    if (numero % 10) == 4:
        return True
    else:
        return False

print(ejercicio1(154))
    
print("\nEJERCICIO 2 \n")

def ejercicio2(numero):
    if (numero >= 100)and(numero < 1000):
        return "El número tiene 3 digitos"
    else:
        return "El número tiene más o menos de 3 digitos"

print(ejercicio2(152))

print("\nEJERCICIO 4\n")

def ejercicio4(numero):
    if (numero >= 10)and(numero < 100):
        from math import floor
        a = floor(numero/10)
        b = numero%10
        return a + b
    else:
        return "Digite un número entero de dos digitos"

print(ejercicio4(34))

print("\nEJERCICIO 6\n")

def ejercicio6(numero):
    if (numero >= 10)and(numero < 20):
        primos = [11,13,17,19]
        if numero in primos:
            return "El número es primo"
        else:
            return "El número NO es primo"
    else:
        return "Digite un numero entero menor a 20 de dos digitos"

print(ejercicio6(11))

print("\nEJERCICIO 7\n")

def ejercicio9(numero):
    if (numero >= 10) and (numero < 100):
        from math import floor
        a = floor(numero/10)
        b = numero%10
        if (a%b == 0) and (b%a == 0):
            return "Ambos digitos son multiplos el uno del otro"
        elif (a%b == 0) or (b%a == 0):
            return "Tiene digitos multiplos"
        else:
            return "NO tiene digitos multiplos"

print(ejercicio9(55))

print("\nEJERCICIO 12\n")

def ejercicio12(num1,num2):
    from math import floor
    a = floor(num1/10)
    b = num1%10
    c = floor(num2/10)
    d = num2%10
    arraynum1 = [a,b]
    if (c in arraynum1) or (d in arraynum1):
        return "tienen digitos comunes"
    else:
        return "NO tienen digitos comunes"

print(ejercicio12(43,23))

print("\nEJERCICIO 17\n")

def ejercicio17(numero):
    if (numero>=100) and (numero<1000):
        from math import floor
        a = floor(numero/100)
        b = floor((numero%100)/10)
        c = numero%10
        array = [a,b,c]
        maximo = max(array)
        return array.index(maximo) + 1 
    else:
        return "Digite un número entero de tres digitos"

print(ejercicio17(145))

print("\nEJERCICIO 20\n")

def ejercicio20(num1,num2,num3):
    array = [num1,num2,num3]
    array.sort()
    return array

print(ejercicio20(8,6,1))

print("\nEJERCICIO 27\n")

def ejercicio27(numero):
    if (numero>999) and (numero<10000):
        from math import floor
        a = floor(numero/1000)
        b = floor((numero%1000)/100)
        c = floor((numero%100)/10)
        d = numero%10
        suma = 0
        if (a%2 == 0):
            suma = suma + 1
        if (b%2 == 0):
            suma = suma + 1
        if (c%2 == 0):
            suma = suma + 1
        if (d%2 == 0):
            suma = suma + 1
                
        return suma
    else:
        return "Digite un número entero de 4 digitos"

print(ejercicio27(7854))

print("\nEJERCICIO 29\n")

def ejercicio29(numero):
    if (numero > 9999) and (numero < 100000):
        from math import floor
        a = floor(numero/10000)
        b = floor((numero%10000)/1000)
        d = floor((numero%100)/10)
        e = numero%10
        suma = 0
        if (a == e):
            suma += 1
        if (b == d):
            suma += 1
        if (suma == 2):
            return "Es un número capicúo"
        else:
            return "NO es un número capicúo"
    else:
        return "Digitar un numero entero de cinco digitos"

print(ejercicio29(15651))

print("\nEJERCICIO 32\n")

def ejercicio32(numero):
    if (numero % 7) == 0:
        return "Es un número multiplo de 7"
    else:
        return "No es un número multiplo de 7"

print(ejercicio32(14))

print("\nEJERCICIO 36 \n")

def ejercicio36(numero):
    if (numero>999) and (numero <10000):
        from math import floor
        a = floor(numero/1000)
        b = floor((numero%1000)/100)
        c = floor((numero%100)/10)
        d = numero%10
        suma = 0
        if (a%2) == 0:
            suma += 1
        if (b%2) == 0:
            suma += 1
        if (c%2) == 0:
            suma += 1
        if (d%2) == 0:
            suma += 1
        if suma > 2:
            return "Tiene más digitos pares"
        if suma == 2:
            return "Tiene iguales digitos pares o impares"
        else:
            return "Tiene más digitos impares"
    else:
        return "Digite un número entero de 4 digitos"

print(ejercicio36(2455))
