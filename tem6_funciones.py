import os
    
def funcion1():
    os.system("cls")
    print("Dame 2 num: ")
    num1 = int(input("Num 1:"))
    num2 = int(input("Num 2:"))
    res=num1+num2
    print(f"La suma de {num1} + {num2} es {res}")

def funcion2():
    print("Adios mundo")

def run():
    os.system("cls")
    print("Menu de opciones:")
    print("1.- Suma de 2 numeros")
    print("2.- Otro")
    print("3.- salir")

    op = int(input("numero: "))

    if op ==1:
        funcion1()
    else:
        funcion2()

if __name__ == "__main__" :
    run()