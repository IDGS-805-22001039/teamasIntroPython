from io import open
import os

class Cine:
    boletos = 0
    total = 0.0
    compradores = 0
    nombre = ""
    boleto = 12
    

    def __init__(self, boletos, compradores, nombre):
        self.boletos = boletos
        self.compradores = compradores
        self.nombre = nombre
        self.total = 0.0
    
    def sin_descuento(self):
        self.total = self.boletos * self.boleto
        print(f"En total pagarás ${self.total}")

    def descuento_10(self):
        self.total = self.boletos * self.boleto
        self.total = self.total - (self.total * 0.10)
        print(f"\nComo compraste {self.boletos} boletos, obtuviste el 10% de descuento. En total pagarás ${self.total}")
    
    def descuento_cineco(self):
        self.total = self.total - (self.total * 0.10)
        print(f"\nComo pagaste con CINECO, obtuviste un 10% extra de descuento. En total pagarás ${self.total}")
    
    def descuento_15(self):
        self.total = self.boletos * self.boleto
        self.total = self.total - (self.total * 0.15)
        print(f"\nComo compraste {self.boletos} boletos, obtuviste el 15% de descuento. En total pagarás ${self.total}")

    def guardar_compra(self):
        if self.compradores == 1:
            texto = f"\n{self.nombre} compró {self.boletos} boletos por una cantidad de ${self.total}"
        else:
            texto = f"\n{self.nombre} y sus {self.compradores} acompañantes compraron {self.boletos} boletos por una cantidad de ${self.total}"

        with open('registro.txt', 'a') as fichero:
            fichero.write(texto)

    def imprimir_ticket(self):
        texto = " "
        with open('registro.txt', 'w') as fichero:
            fichero.write(texto)

def main():
    while True:
        os.system('cls')
        print("\n¿Quién está comprando?")
        nombre = input("Nombre: ")

        print(f"Hola {nombre}, ¿cuántas personas vienen a comprar contigo?")
        compradores = int(input())
        limite = compradores * 7

        print("¿Cuántos boletos quieres comprar?")
        boletos = int(input())

        while boletos > limite:
            print(f"Acción requerida: El número de boletos sobrepasa el límite permitido de comprar por comprador \n 1.-Aumentar el número de compradores \n 2.-Disminuir el número de boletos")
            sel = int(input())
            if sel == 1:
                print("¿Cuántos compradores quieres aumentar?")
                aumento = int(input())
                compradores = compradores + aumento
                limite = compradores * 7
                print(f"Has aumentado {aumento} compradores, ahora son {compradores} compradores")
            elif sel == 2:
                print("¿Cuántos boletos quieres disminuir?")
                disminucion = int(input())
                boletos = boletos - disminucion
                print(f"Has disminuido {disminucion} boletos, ahora son {boletos} boletos")
        
        obj = Cine(boletos, compradores, nombre)
        
        while True:
            print("¿Qué quieres realizar? \n 1.-Pagar \n 2.-Cancelar compra")
            sel_compra = int(input())
            if sel_compra == 2:
                print("Compra cancelada")
                break
            elif sel_compra == 1:
                if boletos > 0 and boletos <= 2:
                    obj.sin_descuento()
                elif boletos >= 3 and boletos <= 5:
                    obj.descuento_10()
                elif boletos > 5:
                    obj.descuento_15()
                
                print(f"¿Cuentas con la Tarjeta CINECO? Esto te dará un 10% extra de descuento \n 1.-Sí \n 2.-No")
                sel_cineco = int(input())
                if sel_cineco == 1:
                    obj.descuento_cineco()
                
                print("Guardando compra...") 
                obj.guardar_compra()
                print("Compra guardada")
                break

        print("¿Deseas realizar otra compra? \n 1.-Sí \n 2.-Salir")
        sel = int(input())
        if sel == 2:
            print("Imprimiendo ticket")
            obj.imprimir_ticket()
            print("¡Gracias por comprar! Saliendo del programa...")
            break

if __name__=="__main__":
    main()
 