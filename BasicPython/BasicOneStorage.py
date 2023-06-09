# First program ......................................
print("Hello World")

# Input program ......................................
x = input("Write whatever what you want and save it \n")

# Variable definition and type 
number = 5
print(type(number))

floatNumber = 3.0
print(type(floatNumber))

string = "Los strings también son variables (en realidad objetos)"
print(type(string))

# Type convertion
x = '427'           # string
print(x)
print(type(x))
y = int(x)          # y is integer
print(y)
print(type(y))
z = float(y) + 0.6  # z is real number
print(z)
print(type(z))
w = str(z)          # w is string
print(w)
print(type(w))

# Arithmetic operations 
number = 3.0            # float number  
print("Number = " + str(number))
number =  number + 2    # Add
print("Add = " + str(number))
number =  number  - 1   # Substraction
print("Substraction = " + str(number))
number =  number * 4    # Multiplication
print("Multiplication = " + str(number))
number =  number ** 4   # Pow
print("Pow = " + str(number))
result = number / 2     # number divided in three
print("Divided = " + str(result))
number = number // 3    # la división exacta se obtiene con doble slash
print(number)
remainder = number % 2  # this is the remainder of number dived divided two
print("Remainder = " + str(remainder))

# Assignments
number = 9
print("Number = " + str(number))
number -= 4     # number = number - 4
print("Number = " + str(number))
number += 3     # number = number + 3
print("Number = " + str(number))
number *= 3     # number = number * 3
print("Number = " + str(number))
number /= 2     # number = number / 2
print("Number = " + str(number))
number //= 2    # number = number // 2
print("Number = " + str(number))
number %= 7     # number = number % 5
print("Number = " + str(number))
number **= 3     # number = number ** 2
print("Number = " + str(number))

# Comparison operators
one = 1
two = 2
three = 3 
# <, <= , >, >=, ==, != 
print(one != two)   # one < two && < three

# String concatenation 
hello = "Hello"
world = "World"
helloWrold = hello + " " + world
print(helloWrold)

# String multiplication
hello = "Hello"
tenHellos = hello * 10
print(tenHellos)

# String indexing 
# -       654321
#         012345
python = "Python"
print("t: " + python[2])
print("t: " + python[-4])

# String slicing
#          -   987654321    
#              012345678
montyPython = "Monty Pyt"
monty = montyPython[:5]         # El limite superior no contiene al elemento
print(monty)
pyt = montyPython[6:]           # el limite inferior si contienen al elemento
print(pyt)
ty_py = montyPython[3:8]
print(ty_py)
print(montyPyhton[2::-1])       #Elimina las posiciones no apuntadas por los multiplos del numero


# in operator 
iceCream = "Ice Cream"      
print("i" in iceCream)  # boolean result


# len()
phrase = '''
It is a really long string
triple-quoted strings are used
to define multi-line strings
'''
print(len(phrase))

print(phrase)

print(phrase[int(len(phrase)/2):])
print(len(phrase[int(len(phrase)/2):]))
print(phrase[: int(len(phrase)/2) + 1])
print(len(phrase[: int(len(phrase)/2) + 1]))

................ Character escaping ........................
text = "Don't worry about the apostrophe"
print(text)
# The name of this ice cream is "sweet 'n' tasty"
text = ' The name of this ice cream is "Sweet \'n\' tasty" '
print(text)

# ................ Basic Methods ............................
name = "Alejandro"
print(name.upper())
print(name.lower())
print(name.lower().count('a'))

# ................ String Formatting ............................
name = "Alejandro"
age = 17
print("Hi " + name + " your age is " + str(age))
print("Hi {} your age is {}".format(name, age))
print("Hi %s your age is %i" %(name, age))

# .................. List ......................................
numbers = [1, 2.0, "three", True]
print(numbers)
print(type(numbers))
print(numbers[3])
print(numbers[-1])
print(type(numbers[3]))
print(numbers[2:])

# .................. List operations .........................
animals = ["dog", "cat", "tiger", "cow", "duck", "bear", "monkey", "bird", "lion"]
print(animals)
animals += ["donkey", "caterpillar"]
print(animals)
animals *= 2
print(animals)
animals.remove("tiger")
print(animals)
animals.append("\n")
print(animals)
# animals.append(["A", "B"])
# print(animals)
animals.sort()
print(animals)
x = animals.pop(1)
print(x)
animals.clear()
print(animals)

# .................. List items (mutables) ...................
animals = ["dog", "cat", "tiger", "cow", "duck", "bear", "monkey", "bird", "lion"]
print(animals)
animals[:3] = ["snake"]
print(animals)
animals[-2:] = []
print(animals)
animals[:] = []
print(animals)

# .................. Tuples (inmutables) ...................
vowels = ('a', 'e', 'i', 'o', 'u')
print(vowels)
print(type(vowels))
print(len(vowels))
x = vowels.__add__(tuple('b'))
print(x)

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
