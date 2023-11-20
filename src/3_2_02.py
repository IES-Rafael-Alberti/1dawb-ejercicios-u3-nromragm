def pedir_datos():   
    usuario = {}

    usuario["nombre"] = input("Ingrese su nombre: ")
    usuario["edad"] = input("Ingrese su edad: ")
    usuario["direccizzzon"] = input("Ingrese su dirección: ")
    usuario["telefono"] = input("Ingrese su número de teléfono: ")
    
    return usuario

def mostrar_datos(usuario):

    mensaje = f"{usuario["nombre"]} tiene {usuario["edad"]} años, vive en {usuario["direccion"]} y su número de teléfono es {usuario["telefono"]}."
    print(mensaje)


def main():
    
    datos = pedir_datos()

    mostrar_datos(datos)


if __name__ == "__main__":
    main()