# print("Curso básico de python")
# x = input("Ingrese lo que usted quiera \n")
# print(x)

# number = 3
# print(type(number))

# floatNumber = 3.0
# print(type(floatNumber))

# string = 'Los strings tambien son variables (realmente objetos)'
# print(type(string))

# x = '123'
# print(x)
# print(type(x))

# y = int(x)
# print(y)
# print(type(y))

# z = float(y + 0.6)
# print(z)
# print(type(z))

# w = str(z)
# print(w)
# print(type(w))

# number = 4.0
# print("El número es: " + str(number))

# number = number + 2
# print(number)

# number = number - 3
# print(number)

# number = number * 4
# print(number)

# number = number ** 2
# print("la potencia es: " + str(number))

# number = number / 10  
# print(number)

# number = number // 3 # la división exacta se obtiene con doble slash
# print(number)

# number = number % 3
# print(number)

# number = 9
# print(number)

# number += 2    # number = number + 2
# print(number)

# number -= 3 
# print(number)

# number *= 4
# print(number)

# number /= 5
# print(number)

# number //= 2
# print(number)

# number **= 3
# print(number)

# one = 1
# two = 2
# three = 3

# print( one == two ) 
# print( two != three )
# print( three > one )
# print(type( three > one ))
# # > >= < <= 
# x = one == three
# print(x)
# print(not x)
# print(type(x))

# hello = 'hello'
# world = 'world'
# helloWorld = hello + " " + world
# print(helloWorld)

# tenHellos = hello * 10
# print(tenHellos + "\n")

# #-            10987654321 
# #+             0123456789
# montyPyhton = "MontyPytho"
# print(montyPyhton)
# # print(montyPyhton[0])
# # print(montyPyhton[-10])
# print(montyPyhton[3:7])
# print(montyPyhton[3:])
# print(montyPyhton[:7])
# print(montyPyhton[:])
# print(montyPyhton[2::-1])  #Elimina las posiciones no apuntadas por los multiplos del numero

# iceCream = "Ice Cream"
# print( "i" in iceCream)
# print( "C" in iceCream)
# print(len(iceCream))

# phrase = "12345"
# print(phrase)
# print(len(phrase))
# x = phrase[:(len(phrase)//2)]
# print(x)
# print(len(x))

# # ................ Character escaping ........................
# text = "Don't worry about the apostrophe"
# print(text)
# # The name of this ice cream is "sweet 'n' tasty"
# text = ' The name of this ice cream is "Sweet \'n\' tasty" '
# print(text)

# # ................ Basic Methods ............................
# name = "Alejandro"
# print(name.upper())
# print(name.lower())
# print(name.lower().count('a'))

# # ................ String Formatting ............................
# name = "Alejandro"
# age = 17
# print("Hi " + name + " your age is " + str(age))
# print("Hi {} your age is {}".format(name, age))
# print("Hi %s your age is %i" %(name, age))

# # .................. List ......................................
# numbers = [1, 2.0, "three", True]
# print(numbers)
# print(type(numbers))
# print(numbers[3])
# print(numbers[-1])
# print(type(numbers[3]))
# print(numbers[2:])

# # .................. List operations .........................
# animals = ["dog", "cat", "tiger", "cow", "duck", "bear", "monkey", "bird", "lion"]
# print(animals)
# animals += ["donkey", "caterpillar"]
# print(animals)
# animals *= 2
# print(animals)
# animals.remove("tiger")
# print(animals)
# animals.append("\n")
# print(animals)
# # animals.append(["A", "B"])
# # print(animals)
# animals.sort()
# print(animals)
# x = animals.pop(1)
# print(x)
# animals.clear()
# print(animals)

# # .................. List items (mutables) ...................
# animals = ["dog", "cat", "tiger", "cow", "duck", "bear", "monkey", "bird", "lion"]
# print(animals)
# animals[:3] = ["snake"]
# print(animals)
# animals[-2:] = []
# print(animals)
# animals[:] = []
# print(animals)

# # .................. Tuples (inmutables) ...................
# vowels = ('a', 'e', 'i', 'o', 'u')
# print(vowels)
# print(type(vowels))
# print(len(vowels))
# x = vowels.__add__(tuple('b'))
# print(x)

# .................. dictionaries ...................
phoneBook = {"pepe" : 123456, "pedro" : 654321, "maria" : 987456}
print(phoneBook)
print(phoneBook["pepe"])
phoneBook["pedro"] = 88888888
print(phoneBook)
del phoneBook["maria"]
print(phoneBook)
x = phoneBook.keys()
z = phoneBook.values()
print(x)
print(type(x))
print(z)
print(type(z))

print('pepe' in phoneBook)