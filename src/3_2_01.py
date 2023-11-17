
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
    if divisa in divisas_simbolo:
        print (f"El simbolo de {divisa} es {divisas_simbolo[divisa]}")
    else:
        print(f"La divisa {divisa} no esta en el diccionario")


def main():
    
    divisas_simbolo = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

    divisa = pedir_divisa()

    comprobar_divisa(divisa, divisas_simbolo)



if __name__ == "__main__":
    main()