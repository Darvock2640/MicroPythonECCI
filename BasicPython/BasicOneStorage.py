"""
# First program ......................................
print("Hola mundo")

# Variable definition and type 
number = 5
print(type(number))

floatNumber = 3.0
print(type(floatNumber))

string = "Los strings también son variables"
print(type(string))

#Type convertion
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

# assignments
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

#Comparison operators
one = 1
two = 2
three = 3 
# <, <= , >, >=, ==, != 
print(one != two)   # one < two && < three

# string concatenation 
hello = "Hello"
world = "World"
helloWrold = hello + " " + world
print(helloWrold)

#string multiplication
hello = "Hello"
tenHellos = hello * 10
print(tenHellos)

# string indexing 
# -       654321
#         012345
python = "Python"
print("t: " + python[2])
print("t: " + python[-4])

#string slicing
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
"""

# len()
phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
print(len(phrase))

print(phrase)

print(phrase[int(len(phrase)/2):])
print(len(phrase[int(len(phrase)/2):]))
print(phrase[: int(len(phrase)/2) + 1])
print(len(phrase[: int(len(phrase)/2) + 1]))