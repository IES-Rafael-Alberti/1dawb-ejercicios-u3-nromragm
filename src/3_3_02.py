def pedir_alumnos():
    alumnos = []
    salir = False
    while not salir:
        nombre = input("Introduce un nombre (escribe x para terminar): ")
        if nombre.lower() == "x":
            salir = True
        else:
            alumnos.append(nombre)

    return alumnos


def mostrar_sin_repeticiones(alumnos_primaria, alumnos_secundaria):
    print(f"Nombres sin repeticiones:\n{alumnos_primaria + alumnos_secundaria}")


def mostrar_repetidos(alumnos_primaria, alumnos_secundaria):
    repetidos = set(alumnos_primaria) & set(alumnos_secundaria)
    
    print(f"Nombres que se repiten entre primaria y secundaria:\n{repetidos}")


def mostrar_no_repetidos(alumnos_primaria, alumnos_secundaria):
    no_repetidos = set(alumnos_primaria) - set(alumnos_secundaria)
    
    print("Nombres de primaria que no se repiten en secundaria:")
    print(no_repetidos)


def main():
    print("Alumnos de Primaria:")
    alumnos_primaria = pedir_alumnos()

    print("\nAlumnos de Secundaria:")
    alumnos_secundaria = pedir_alumnos()

    mostrar_sin_repeticiones(alumnos_primaria, alumnos_secundaria)
    mostrar_repetidos(alumnos_primaria, alumnos_secundaria)
    mostrar_no_repetidos(alumnos_primaria, alumnos_secundaria)

if __name__ == "__main__":
    main()

