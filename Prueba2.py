print("2 prueba")

print("\n Listas")

words = ["Yarly"," la niña ", " más ", "linda"]
print(words[0], words[1])

number = 3
things = ["string", 0, [1,2,number],4.56]
print(things[2])

nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 2)

print("\n Operador in")

words = ["spam","egg","spam","sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
print("el operador not")
print(not "tomato" in words)
print("tomato" not in words)

print("\n El operador in puede tambien ser utilizado para determinar \n si una cadena es subcadena de otra")

cadena1 = "Yarly es la niña más linda del mundo"
print("Yarly" in cadena1)

print("\n Método append")

frase = ["Yarly","estudia","estadística", "en"]
frase.append("Univalle")
print(frase)

print("\n también se usa con numeros")
numeros = [1,2,3,4]
numeros2 = [6,7,8]
numeros.append(5)
numeros.append(numeros2)
print(numeros)
print("\n yo puedo agregar una lista a una lista igualmente con append \n y accedo al elemento de esa lista de la siguiente forma")
print(numeros[5][0])

print("\n Método insert")
words = ["Python","fun"]
words.insert(1,"is")
print(words)

print("\n Método index")
letters =["p","q","r","s","p","u"]
print(letters.index("r"))
print(letters.index("s"))

print("\n prueba de if")

words = ["spam","egg","spam","sausage"]
if "sausage" in words:
    posicion = words.index("sausage")
    print("Si está, y está en la posición " + str(posicion))
else:
    print("No está en words")
    

print("\n Función len")

print("\n función len")
frase1 = "la niña"
print(len(frase1))


print("\n Otras funciones y métodos")

words = ["spam","egg","spam","sausage"]
print("\n Método count")
print(words.count("spam"))
words.append("bread")
words.remove("egg")
print(words)
words.reverse()
print(words)

numeros = list(range(10))
print(numeros)
numbers = list(range(3,8))
print(numbers)
