def producto_matrices(a, b):
    resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):   
            resultado[i][j] += a[i][j] * b[i][j]

    for i in range(len(resultado)):
        resultado[i] = tuple(resultado[i])
    resultado = tuple(resultado)

    return resultado


def main():
    a = ((1, 2,),
         (3, 4,),
         (5, 6))

    b = ((-1, 0),
         (0, 1),
         (1, 1))

    resultado = producto_matrices(a, b)

    for i in range(len(resultado)):
        print(resultado[i])

if __name__ == "__main__":
    main()
