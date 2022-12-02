"""
#Character escaping
dontWorry = "Don't worry about apostrophes"
print(dontWorry)

# The name of this ice-cream is "Sweet 'n' Tasty"
print("The name of this ice-cream is \"Sweet 'n' Tasty\"")

# Basic methods
name = "Alejandro"
print(name)
print(name.upper())
print(name.lower())
print(name.lower().count('a'))

# String formatting
name = "Pepito Pérez"
years = 16
print("Hello, Python! My name is %s" % name)
print("I'm %i years old" % years)
print("Hello python! My name is {} and I'm {} years old".format(name, years))

# list
numbers = [1, 4, 23, 6, 3.54, "uno"]
print(numbers)
print(type(numbers))
print(numbers[3])
print(type(numbers[3]))
print(numbers[2:5])

# list operations
animals = ['elephant', 'lion', 'mouse', 'horse', 'fish', 'dolphin']
print(animals)
animals += ['dog', 'cat']
print(animals)
#animals *= 2
#print(animals)
animals.append("snake")
print(animals)
animals[2] = "monkey"
print(animals)

#input
X = input("Ingrese lo que sumercé considere necesario y luego oprima enter \n")
print(X)
print(type(X))
nX = int(X)
print(nX)
print(type(nX))

# list items (mutable)
animals = ['elephant', 'lion', 'mouse', 'horse', 'fish', 'dolphin']
print(animals)
animals[1:3] = ["cat"]
print(animals)
animals[3:] = []
print(animals)
animals[:] = []
print(animals)

#Tuples (inmutable)
vowels = ('A', 'E', 'I', 'O', 'U')
print(vowels)
print(len(vowels))

# Dictionaries
phoneBook = {"Pepe" : [1,2,3,4,5,6], "Juan" : 2445873, "Pedro" : 7263434}
print(phoneBook)
phoneBook["Juan"] = 1233211
print(phoneBook)
phoneBook["Maria"] = 9887766
print(phoneBook)
del phoneBook["Pedro"]
print(phoneBook)
print(phoneBook.values())
print(phoneBook.keys())

# in keyword
phoneBook = {"Pepe" : [1,2,3,4,5,6], "Juan" : 2445873, "Pedro" : 7263434}
print(2445873 in phoneBook.values())

# conditions and boolean operators
name = "Juan"
age = 24
print(name == "pedro" or age > 25)
print(name == "Juan" and age < 5)
print(name == "Juan" or not name == "Maria" and age > 16)

# if elif
name = "pepe"
age = 35
if name == "maria" and age > 15:
    print("si se llama pepe y tiene mas de 15")
elif name == "pepo":
    print("si se llama así pero no tiene la edad")
elif age > 45:
    print("Si tiene la edad pero no se llama así")
else:
    print("Ese man no era")

#for loop
helloWorld = "Hello World"

for letra in helloWorld:
    print(letra)

myList = [1, "Esto no", 4, 6, 45.26 , -4]

temp = []

for elemento in myList:
    temp.append(type(elemento))

print(temp)

temp2 = []
for elemento in myList:
    temp2.append(elemento)
print(temp2)

for n in range(11):
    print(n*10)

#while

square = 1

while square <= 10:
    print(square)
    square += 1

print("finished")

square = 0
number = 1

while number < 10:
    square = number ** 2
    print(square)
    number += 1

# break keyword
count = 0

while True:
    print(count)
    count += 1
    if count >= 12:
       break

zoo = ['lion', 'tiger', 'elephant', 'monkey', 'snake', 'giraffe']

while True:
    animal = zoo.pop()
    print(animal)
    print(zoo)
    if animal == "elephant":
        break

zoo = ['lion', 'tiger', 'elephant', 'monkey', 'snake', 'giraffe']
zoo2 = []
#   0 hasta 5
for i in range(len(zoo)):
    zoo2.append(zoo.pop())

print(zoo2)

#continue keyword
for i in range(10):
    if i == 5:
        continue
    else:
        print(i)

for i in range(11):
    if i % 2 != 0:
        continue
    else:
        print(i)
"""