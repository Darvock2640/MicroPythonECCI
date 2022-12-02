# Functions

def HelloWorld():
    print("Hello World") 

HelloWorld()

# Arguments
def Square(base):
    print(base**2)

Square(5)
Square(1000)
Square(3)

# Return
def Sum2Numbers(a, b):
    return a + b

x = Sum2Numbers(2, 3)
print(x)

# Default parameters
def Sum2Numbers(a = 0, b = 0):
    return a+b

print(Sum2Numbers())

def Subs2Numbers (a = 0, b = 0):
    return a - b

print(Subs2Numbers(b = 3.5, a = 5))
print(Subs2Numbers(4, 5))

# Class and objects
class MyClass:
    def __init__(self, inner_variable = 0):
        self.innerVariable = inner_variable
    def Print(self):
        print(self.innerVariable)

myObject = MyClass(-45)             # Esta es la forma de crear un objeto a partír de una clase (instanciar)
myObject.Print()                    # Se puede acceder a los miembros de un objeto (atributos, metodos) usando el operador "."
myObject.innerVariable = 65535
myObject.Print()

# Class and object example
class Car():
    def __init__(self, brand = "Toyota", color = "", motor_CC = 0, model = 0, kind = "", cost = 0.0):
        self.color = color
        self.motorCC = motor_CC
        self.model = model
        self.kind = kind
        self.brand = brand
        self.cost = cost
    def Print(self):
        temp = '''
Kind: {}
Brand: {}
Model: {}
Color: {}
Motor: {} cc
Cost: ${}
        '''.format(self.kind, self.brand, self.model, self.color, self.motorCC, self.cost)
        print(temp)

    def __str__(self) -> str:
        return '''
Kind: {}
Brand: {}
Model: {}
Color: {}
Motor: {} cc
Cost: ${}
            '''.format(self.kind, self.brand, self.model, self.color, self.motorCC, self.cost)
        

car1 = Car()
print(car1)
car2 = Car(color="red", motor_CC=1100, model=1998, kind="Van", cost=5000)
car2.Print()

# Modules
import datetime, time
import time as r
from time import sleep as retardo

print(datetime.datetime.today())

for i in range(10):
    print(i)
    retardo(.25)
    r.sleep(.25)
    time.sleep(.25)