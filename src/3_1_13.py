def pedir_numeros():
    salir = False
    lista = []
    while not salir:
        try:
            numero = int(input("Introduce numeros (0 para salir)"))
            if numero == 0:
                salir = True
            else:
                lista.append(numero)

        except:
            print("Numero introducido no valido")

    return lista

def calcular_media(lista):
    return sum(lista) / len(lista)


def main():
    lista = pedir_numeros()
    
    print(calcular_media(lista))


if __name__ == "__main__":
    main()