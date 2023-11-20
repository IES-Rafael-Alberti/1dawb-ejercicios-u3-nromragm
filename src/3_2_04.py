MESES = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

def pedir_fecha():
    todo_ok = False

    while not todo_ok:
        try:
            fecha = input("Introduce una fecha en formato dd/mm/yyy: ")
            list_fecha = fecha.split("/")
            if len(list_fecha[2]) == 4 and len(list_fecha[1]) and len(list_fecha[0] == 2):
                todo_ok = True
            else:
                raise ValueError
        except:
            print("Introduce una fecha valida")

    return fecha


def mostrar_fecha(fecha):
    nueva_fecha = 


def main():
    fecha = pedir_fecha()

    mostrar_fecha(fecha)


if __name__ == "__main__":
    main()