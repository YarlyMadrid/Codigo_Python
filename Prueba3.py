print("FUNCIONES")

def my_fun():
    print("Yarly aprende python")
    print("Yarly aprende Javascript también")

my_fun()

def max(x,y):
    if x>=y:
        return x
    else:
        return y

print(max(4,7))

def shortest_string(x,y):
    if len(x)<=len(y):
        return x
    else:
        return y

z = shortest_string([4,7,8],[4,2])
print(z)

print("Cómo comentar funciones")

def shout(word):
    """
    print a word with an
    exclamation mark following it.
    """
    print(word + "!")

print(shout("spam"))

print("\n LAS FUNCIONES TAMBIÉN PUEDEN SER UTILIZADAS COMO ARGUMENTOS DE OTRAS FUNCIONES \n")

def add(x,y):
    return x+y

def do_twice(func,x,y):
    return func(func(x,y),func(x,y))

a = 5
b = 10

print(do_twice(add, a,b))
print(add(5,10))

print("veamos otro ejemplo")
def square(x):
    return x*x

def test(func,x):
    print(func(x))

test(square, 42)

print(" \n MODULOS \n")

import random

for i in range(5):
    value = random.randint(1,6)
    print(value)

print("respuesta a pregunta")
def print_nums(x):
    for i in range(10):
        print(i)
        return

print_nums(10)
    
print("\n respuesta a otra pregunta")

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(4))
