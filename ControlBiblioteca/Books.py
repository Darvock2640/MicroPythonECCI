import datetime

class Book ():
    def __init__(self, tittle, author, sort, editor, edition, stock, id = 0) -> None:
        self.id = id
        self.tittle = tittle
        self.author = author
        self.sort = sort
        self.editor = editor
        self.edition = edition 
        self.stock = stock
        self.user = []

        print("The book was created succesfully")
    
    def BookBorrow(self) -> str:
        if self.stock > 0:
            self.stock -= 1
            self.user.append(self.UserData())
            return "The book was borrowed succesfully"
        else:
            return "The book does not have stock"

    def BookBack(self):
        if len(self.user) == 0:
            return "There is no books borrowed"
        else:
            userId = int(input("\nIngrese el documento del cliente\n"))
            for i in range(len(self.user)):
                if self.user[i]["UserId"] == userId:
                    self.stock += 1
                    if len(self.user) == 1:
                        self.user = []
                    else:
                        self.user[i :] = self.user[i+1 :]
                    break
            return "The book was returned succesfully"

    def UserData (self) -> dict:
        user = str(input("\nIngrese el nombre del cliente\n"))
        userId = int(input("\nIngrese el documento del cliente\n"))
        date = datetime.datetime.today()
        return {"Name": user, "UserId": userId, "Date": str(date)}

    def __str__(self) -> str:
        return """
ID: {}
Tittle: {}
Author: {}
Sort: {}
Editor: {}
Edition: {}
Stock: {}
        """.format(self.id, self.tittle, self.author, self.sort, self.editor, self.edition, self.stock)
