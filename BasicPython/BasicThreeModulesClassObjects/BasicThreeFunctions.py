# # ................. functions ........................
# def HelloWorld():
#     print("Hello wolrd!")

# HelloWorld()

# # ................. functions args ....................
# def Adder(A, B):
#     print("El resultado es: "  + str(A + B))

# Adder(A = 1, B = 2)

# # ................. init args .....................
# def Adder(A = 0, B = 0):
#     print("El resultado es: "  + str(A + B))

# Adder()

# # ................. docu args .....................
# def Adder(A = int, B = int):
#     print("El resultado es: "  + str(A + B))

# Adder(2 , 0)

# # ................. return .....................
# def Adder(A = int, B = int):
#     return A + B

# print(Adder(2 , 0))

# # ................. docu return .....................
# def Adder(A = int, B = int) -> int:
#     return A + B

# print(Adder(3, 4))

# # ................. variable scope ....................
# pepe = None  #Global

# def Adder(A = int, B = int) -> int:
#     print(pepe)
#     juan = 3
#     print(juan)     #local   
#     return A + B

# print(Adder(3, 4))
# print(pepe)


