def pedir_numeros_ganadores():

    numeros = []

    for i in range(6):
        salir = False
        while not salir:
            try:
                numero = int(input(f"Introduce el {i + 1} número ganador del 1 al 49: "))
                
                if numero < 0 or numero > 49:
                    raise ValueError
                else:
                    if numero in numeros:
                        raise ValueError
                    else:
                        numeros.append(numero)
                        salir = True
            except:
                print("Introduce un numero valido")        

    return numeros


def pedir_reintegro():
    reintegro = []
    salir = False

    while not salir:
        try:    
            reintegro = int(input("Introduce un reintegro del 1 al 9: "))
            if reintegro < 1 or reintegro > 9:
                raise ValueError
            else:
                salir = True

        except:
            print("Introduce un numero valido")

    return reintegro


def numeros_ordenados(numeros):

    numeros_ordenados = sorted(numeros)

    resultado = "\nNúmeros ganadores ordenados:\n"

    for numero in numeros_ordenados:
        resultado += str(numero) + ", "
    
    resultado = resultado[:-2] + "."
    
    return resultado


def main():

    numeros_ganadores = pedir_numeros_ganadores()
    reintegro = pedir_reintegro()
    
    print(numeros_ordenados(numeros_ganadores))

    print(f"El reintegro es: {reintegro}")


if __name__ == "__main__":
    main()