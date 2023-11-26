FRUTAS = {"Platano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}

def pedir_fruta_kg():
    todo_ok = False

    while not todo_ok:
        try:
            fruta = input("Introduce la fruta: ")
            kg = int(input("Introduces la cantidad de kilos: "))
            fruta = fruta.capitalize()
            if fruta in FRUTAS:
                if kg < 0:
                   raise ValueError
                else:
                    todo_ok = True
            else:
                raise ValueError
        except:
            print("Introduce una fruta o kg validos")

    return fruta, kg


def mostrar_precio(fruta, kg):
    precio = FRUTAS[fruta] * kg

    print(f"El precio de {kg}kg de {fruta} es {precio}$")


def main():
    fruta, kg = pedir_fruta_kg()

    mostrar_precio(fruta, kg)


if __name__ == "__main__":
    main()