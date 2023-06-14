import DataModel
import DataModel as D
from DataModel import MyClass
from DataModel import MyClass as C

# myObject = DataModel.MyClass()            #Crear un objecto a partir de una clase (instanciar)
# print(myObject.number)          #Apuntar a un atributo del objeto
# myObject.Print()                #Usar un método del objeto

# myObject.number = 25
# print(myObject.number)
# myObject.Print()

# print(DataModel.MyClass.number)           #Apuntar al tributo original de la clase (sin necesidad de instanciar )

# myObject = D.MyClass()            #Crear un objecto a partir de una clase (instanciar)
# print(myObject.number)          #Apuntar a un atributo del objeto
# myObject.Print()                #Usar un método del objeto

# myObject.number = 25
# print(myObject.number)
# myObject.Print()

# print(D.MyClass.number)  

# myObject = MyClass()            #Crear un objecto a partir de una clase (instanciar)
# print(myObject.number)          #Apuntar a un atributo del objeto
# myObject.Print()                #Usar un método del objeto

# myObject.number = 25
# print(myObject.number)
# myObject.Print()

# print(MyClass.number)  

# myObject = C()            #Crear un objecto a partir de una clase (instanciar)
# print(myObject.number)          #Apuntar a un atributo del objeto
# myObject.Print()                #Usar un método del objeto

# myObject.number = 25
# print(myObject.number)
# myObject.Print()

# print(C.number)  

# myObjectOne = DataModel.MyClass()
# myObjectOne.Print()
# myObjectTwo = DataModel.MyClass()
# myObjectTwo.Print()
# myObjectOne.number = 1
# myObjectOne.Print()
# myObjectTwo.number = 2
# myObjectTwo.Print()

objectOne = DataModel.MyClassTwo(id = 1234, name = "One")
objectOne.Print()
print(objectOne.SetId("otra cosa"))
objectOne.Print()
print(objectOne.SetId(456))
objectOne.Print()
print(objectOne.GetId())

