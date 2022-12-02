# Conditions and boolean operators
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

# for loop
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

# while

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

# Break keyword
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

for i in range(len(zoo)):       # Este for realiza 6 iteraciones ya que el tamaño de zoo es 6, es decir (0, 5)
    zoo2.append(zoo.pop())

print(zoo2)

# Continue keyword
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
