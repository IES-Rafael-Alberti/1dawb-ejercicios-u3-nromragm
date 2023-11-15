def lista():
    numeros = list(range(1, 11))

    return numeros


def lista_inversa(lista):
    list_inversa = ", ".join(map(str, reversed(lista)))
    
    return list_inversa


def main():
    numeros = lista()

    print(lista_inversa(numeros))


if __name__ == "__main__":
    main()