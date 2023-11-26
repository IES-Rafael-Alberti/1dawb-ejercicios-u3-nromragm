def producto_escalar(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))


def main():

    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]

    resultado = producto_escalar(vector1, vector2)

    print(f"El producto escalar de los vectores {vector1} y {vector2} es: {resultado}")


if __name__ == "__main__":
    main()
