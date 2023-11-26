def lista_asignaturas():
    list = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    resultado = "Yo estudio: "
    for i in list:
        resultado += i + ", "
        
    resultado = resultado[:-2] + "."
    
    return resultado


def main():
    print(lista_asignaturas())


if __name__ == "__main__":
    main()