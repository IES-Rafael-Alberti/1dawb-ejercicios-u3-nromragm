def lista():
    numeros = list(range(1, 11))

    return numeros


def lista_inversa(lista):
    list_inversa = ', '.join(map(str, reversed(lista)))
    print(list_inversa)


def main():
    # Obtener la lista de números
    numeros = lista()

    # Imprimir la lista en orden inverso separados por comas
    lista_inversa(numeros)


if __name__ == "__main__":
    main()