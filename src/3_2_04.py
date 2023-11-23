MESES = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

def pedir_fecha():
    todo_ok = False

    while not todo_ok:
        try:
            fecha = input("Introduce una fecha en formato dd/mm/yyy: ")
            dia, mes, año = fecha.split("/")
            if len(año) == 4 and len(mes) == 2 and len(dia) == 2:
                if int(dia) < 0 or int(dia) > 31:
                    raise ValueError
                else:
                    if int(mes) < 0 or int(mes) > 12:
                        raise ValueError
                    else:
                        todo_ok = True
            else:
                raise ValueError
        except:
            print("Introduce una fecha valida")

    return dia, mes, año


def mostrar_fecha(dia, mes, año):
    print(f"{dia} de {MESES[int(mes)]} de {año}")


def main():
    dia, mes, año = pedir_fecha()

    mostrar_fecha(dia, mes, año)


if __name__ == "__main__":
    main()