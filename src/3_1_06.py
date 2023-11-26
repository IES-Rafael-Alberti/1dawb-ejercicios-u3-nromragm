def pedir_notas(asignaturas):

    notas = []

    for asignatura in asignaturas:
        salir = False
        while not salir:
            try:
                nota = int(input(f"Introduce la nota de {asignatura}: "))
                if nota < 0 or nota > 10:
                    raise ValueError
                else:
                    notas.append((asignatura, nota))
                    salir = True
            except:
                print("Introduce una nota valida")    

    return notas


def asignaturas_suspendidas(notas):
    suspendidas = []
    
    for asignatura, nota in notas:
        if nota < 5:
            suspendidas.append(asignatura)

    if len(suspendidas) == 0:
        resultado = print("No has suspendido ninguna asignatura")

        return resultado


    else:
        resultado = print("Asignaturas supendidas: ")
        
        return resultado, suspendidas
    

def main():

    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    notas = pedir_notas(asignaturas)

    print(asignaturas_suspendidas(notas))


if __name__ == "__main__":
    main()
