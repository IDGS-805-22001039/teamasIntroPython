class OperasBas:
    #Declaracion de propiedasdes
    num1=0
    num2=0
    #Declaracion del constructor
    def __init__(self, a,b):
        self.num1=a
        self.num2=b

    #Declaracion de los metodos
    def suma(self):
        self .res=self.num1+self.num2
        print(f"La suma es: {self.res}")

def main():
    obj = OperasBas(11111111,11111111)
    obj.suma()

if __name__=="__main__":
    main()
