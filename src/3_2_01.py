
def pedir_divisa():
    salir = False
    while not salir:
        try:
            divisa = input("Introduce una divisa: ")
            if divisa.isalpha():
                divisa = divisa.replace(" ", "").lower().title()
                salir = True
            else:
                raise ValueError

        except:
            print("ERROR")

    return divisa

def comprobar_divisa(divisa, divisas_simbolo):
    return divisas_simbolo.get(divisa)

def mostrar_simbolo(divisa, simbolo):

    if simbolo:
        print(f"El simbolo de {divisa} es {simbolo}")

    else:
        print(f"La divisa {divisa} no esta en el diccionario")    


def main():
    
    divisas_simbolo = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

    divisa = pedir_divisa()

    simbolo = comprobar_divisa(divisa, divisas_simbolo)

    mostrar_simbolo(divisa, simbolo)

if __name__ == "__main__":
    main()