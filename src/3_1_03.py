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
                    notas.append(nota)
                    salir = True
            except:
                print("Introduce una nota valida")    

    return notas

def mostrar_notas(asignaturas, notas):
    print("")
    resultado = ""

    for i in range(len(asignaturas)):
        resultado += f"En {asignaturas[i]} has sacado un {notas[i]}.\n"

    return resultado    

def main():

    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    notas = pedir_notas(asignaturas)

    print(mostrar_notas(asignaturas, notas))

if __name__ == "__main__":
    main()
