x = 5
variable = 30
_variable = 40
y, z, m = 1,2,3

# tipos de datos 

numero = 1
decimal = 1.0978
texto = "esto es una cadena de texto"
booleana = True
booleana = False

cadena = "10"

# convierte una cadena en un entero equivalente

cadena2 = int(cadena)

# conviete un numero en una cadena de texto

cadena3 = str(cadena2)

# convierte un numero en una cadena decimal

cadena4 = float(cadena3)

x = 1
y = x
y = 1

# operaciones entre variables

x = 4
y = 5
x + y
x - y
x * y
x / y
x % y

x = "cadena"
y = "cadena"

z = x + 5

print(z)


x = 5
x = x + 1
x += 1

print(x)

# salidas por pantalla

x = "Hola mundo"
y = "Hola"

print(x, y, "Chao", 3)

# Librerias

import random

random.randint(1, 5)

2

from random import randint

randint(1, 5)

3

from random import *

randint(1, 5)
random()

# Pedir datos al usuario

x = input("ingresa un valor numerico: ")

print(x)

# Condicionales

x = 5
y = 4

print(x < y)
print(x == y)
print(x >= y)
print(x != y)
print(x or y, x and y)

# ej

x = 5
y = 4

print(False and True)

# ej2

x = 5
y = 4

print(x >= 5 and y == 4)

#ej3

import random 

x = random.randint(1, 5)

if x == 1: 
    print("Hola soy el numero 1")

elif x == 2:
    print("Hola soy el numero 2")

else:
    print("Hola soy algun otro numero")

# Lazos

import random

x = 0

x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)
x = x + random.randint(1, 5)

print(x)

#ej 

x = 0

for i in range(10):
    print(i)
    x += random.randint(1, 5)

print(x)

#ej2

import random

x = random.randint(1, 100)
while x!= 5:
    print(random.randint(1, 100))
    continue
    break

print(x)

# Tuplas

numeros = [9, 6, 1, 3, 5]
numeros[0] += 10

print ( numeros)

#ej

numeros = [9, 6, 1, 3, 5]
print(len(numeros))
print(numeros)

#ej2

numero = [9, 6, 1, 3, 5]
print (numeros.index(6))
print(numeros)

#ej3

numeros = [9, 6, 1, 3, 5]
numeros.sort()
numeros.reverse()

print(numeros)

#ej4

numeros = [9, 6, 1, 3, 5]
for elem in numeros:
 print(elem)

#ej5

 numeros = [9, 6, 1, 3, 5]

 for i in range(len(numeros)):
  print(numeros [i]) #indices

  for elem in numeros:
     print(elem) #valores

#cadenas de texto

cadena = "Hola Mundo"

for c in cadena:
   print(c)

#ej

cadena = "Hola Mundo"

print(cadena.upper())

#ej2

cadena = "Hola Mundo"

print(cadena.lower())

#ej3

cadena = "Hola Mundo"

print(cadena.startswith("Hola"))

#Tuplas

variable = (1, 5, 9)

print(type(variable))

tupla = tuple(variable)

print(type(tupla))

#Conjuntos

Lista = [1, 5, 9]
conjunto = {1, 5, 9}

conjunto.add(9)

print(conjunto)

#ej

Lista = [1, 5, 9]
conjunto = {1, 5, 9}

conjunto.remove(9)

print(conjunto)

#ej2

conjunto = {1, 5, 9}

for element in conjunto:
 print(elem)

print(conjunto)

#ej3

conjunto = {1, 5, 9}
conjunto = {1, 5, 10}

print(5 in conjunto)
print(conjunto)

#Diccionarios

d = {
   "nombre": "Marco",
   "edad": 19
}

d["edad"] + 20

d["apellido"] = "Perez"
del d["edad"]
print (d)

#ej

d = {
   "nombre": ["Hola Mundo", 19],
   "edad": {
      "edad de papa": 20, 
      "nombre2": "alonso"
   }
}

print(d["nombre"][1])
