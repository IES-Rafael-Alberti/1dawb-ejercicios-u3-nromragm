def main():

    creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    
    total_creditos = 0
    
    for asignatura, creditos in creditos_asignaturas.items():
        print(f"{asignatura} tiene {creditos} creditos")
        total_creditos += creditos

    print(f"El numero total de creditos es {total_creditos}.")


if __name__ == "__main__":
    main()