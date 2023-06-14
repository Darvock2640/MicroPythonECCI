class MyClass:
    number = 0
    def Print(self):
        print(self.number)

myObject = MyClass()            #Crear un objecto a partir de una clase (instanciar)
print(myObject.number)          #Apuntar a un atributo del objeto
myObject.Print()                #Usar un método del objeto

myObject.number = 25
print(myObject.number)
myObject.Print()

print(MyClass.number)           #Apuntar al tributo original de la clase (sin necesidad de instanciar )

