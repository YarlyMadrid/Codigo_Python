print("Sentencia if")
print(" \n 1ra prueba")
if 10>5:
    print("10 greater than 5")
print("program ended")

print(" \n 2da prueba")

spam = 7
if spam > 5:
    print("five")
if spam > 8:
    print("eigth")

print(" \n 3ra prueba")

num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")
        if num == 12:
            print("tambien es 12")
    
print(" \n 4ta prueba")
num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num == 7:
            print("7")
            
print(" \n 5ta prueba")
num = 7
if num == 7:
    print("7")

print(" \n Sentencia else")
print(" \n 6ta prueba")

num = 7
if num == 5:
    print("number is 5")
else:
    if num == 11:
        print("number is 11")
    else:
        if num == 7:
            print("number is 7")
        else:
            print("number isn't 5, 11 or 7")

print(" \n 7 prueba")
num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num == 7:
            print("7")

print(" \n BUCLES")

print(" \n 8 prueba")
i = 3
while i>=0:
    print(i)
    i=i-1
