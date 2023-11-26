def seguir_comprando():
    todo_ok = False
    while not todo_ok:
        try:
            seguir = input("Quieres seguir comoprando? (s/n): ").lower()
            if seguir == "s" or seguir == "n":
                todo_ok = True
            else:
                raise ValueError    
        except:
            print("Error, Introduzca una respuesta valida (s/n)")
    
    return seguir

def añadir_articulo(cesta_compra, articulo):
    todo_ok = False
    while not todo_ok:
        try:
            precio = float(input(f"Introduce el precio de {articulo}: "))
            if precio > 0:
                todo_ok = True
            else:
                raise ValueError    
        except:
            print("Error, Introduzca un precio valido")

    cesta_compra[articulo] = precio
    return cesta_compra

def total_compra(cesta_compra):
    total = sum(cesta_compra.values())

    return total

def main():

    cesta_compra = {}

    seguir = "s"

    while seguir == "s":
        articulo = input("Introduce el articulo: \n").title()
        cesta_compra = añadir_articulo(cesta_compra, articulo)

        print(cesta_compra)

        seguir = seguir_comprando()

    precio_total = total_compra(cesta_compra)
    print(f"El precio total es de {precio_total}$")


if __name__ == "__main__":
    main()