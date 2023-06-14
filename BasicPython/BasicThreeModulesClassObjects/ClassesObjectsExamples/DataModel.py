class MyClass:
    number = 0
    def Print(self):
        print(self.number)

class MyClassTwo(MyClass):
    def __init__(self, id = 0000, name = str) -> None:
        self.id = id 
        self.name = name

    def SetId(self, id = int) -> str:
        if type(id) is int:
            self.id = id
            return "ok"
        else:
            return "The arg was no a int variable"
        
    def GetId(self):
        return self.id

    def __str__(self) -> str:
        text = """
        The name of the object is {}
        The id of the object is {}
        The number of the objcet is {}
        """.format(self.name, self.id, self.number)

        return text
    
    def Print(self):
        print(self.__str__())
    