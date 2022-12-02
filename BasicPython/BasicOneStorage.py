# First program ......................................
print("Hola mundo")

# Variable definition and type 
number = 5
print(type(number))

floatNumber = 3.0
print(type(floatNumber))

string = "Los strings también son variables"
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
number =  number ** 4    # Multiplication
print("Pow = " + str(number))
result = number / 2     # number divided in three
print("Divided = " + str(result))
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

# Character escaping
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

# List
numbers = [1, 4, 23, 6, 3.54, "uno"]
print(numbers)
print(type(numbers))
print(numbers[3])
print(type(numbers[3]))
print(numbers[2:5])

# List operations
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

# Input
X = input("Ingrese lo que sumercé considere necesario y luego oprima enter \n")
print(X)
print(type(X))
nX = int(X)
print(nX)
print(type(nX))

# List items (mutable)
animals = ['elephant', 'lion', 'mouse', 'horse', 'fish', 'dolphin']
print(animals)
animals[1:3] = ["cat"]
print(animals)
animals[3:] = []
print(animals)
animals[:] = []
print(animals)

# Tuples (inmutable)
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