import os

FICHAS = (" ", "X", "O")

POSICIONES_POSIBLES = (
    (
        {(0, 1), (1, 0), (1, 1)},
        {(0, 0), (0, 2), (1, 1)},
        {(0, 1), (1, 1), (1, 2)}
    ),
    (
        {(0, 0), (1, 1), (2, 0)},
        {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 2)}
    ),
    (
        {(1, 0), (1, 2), (2, 1)},
        {(1, 1), (2, 0), (2, 2)},
        {(1, 1), (1, 2), (2, 1)}
    )
)
def clear_console():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def crear_fila() -> list:
    return list(0 for _ in range(3))


def crear_tablero() -> tuple:
    return tuple(crear_fila() for _ in range(3))


def mostrar_tablero(tablero):
    clear_console()
    print("-" * 13)

    for fila in tablero:
        mostrar_fila(fila)
        print("-" * 13)


def mostrar_fila(fila: list):
    contenido_fila = "| "
    for celda in fila:
        contenido_fila += FICHAS[celda] + " | "
    print(contenido_fila)


def cambiar_turno(turno: int, ronda: int) -> tuple:
    if turno % 2 == 0:
        ronda += 1
        turno = 1

        print(f"\nRONDA {ronda}")
    else:
        turno = 2
        print(f"\nRONDA {ronda}")
    return turno, ronda


def pedir_posicion() -> tuple:
    filafalse = False
    columnafalse = False

    while not filafalse:
        try:
            fila = int(input("Introduce la posición de la fila (1, 2 o 3): ")) - 1
            if fila < 0 or fila > 2:
                raise ValueError

            else:
                filafalse = True

        except ValueError:
            filafalse = False
            print("ERROR! Introduce un numero valido")

    while not columnafalse:
        try:
            columna = int(input("Introduce la posición de la columna (1, 2 o 3): ")) - 1
            if columna < 0 or columna > 2:
                raise ValueError

            else:
                columnafalse = True

        except ValueError:
            columnafalse = False
            print("ERROR! Introduce un numero valido")

    return fila, columna


def comprobar_movimiento(tablero, fila, columna) -> bool:
    for posicion in POSICIONES_POSIBLES[fila][columna]:
        if tablero[posicion[0]][posicion[1]] == 0:
            movimiento_posible = True
            return movimiento_posible
        else:
            movimiento_posible = False
    return movimiento_posible


def colocar_ficha(tablero: tuple, turno: int, ronda: int):
    posicion_ficha = {"fila": None, "columna": None}
    loop = True
    while loop:
            
        print(f"Jugador {turno}")
        posicion_ficha["fila"], posicion_ficha["columna"] = pedir_posicion()

        if tablero[posicion_ficha["fila"]][posicion_ficha["columna"]] == 0:
            tablero[posicion_ficha["fila"]][posicion_ficha["columna"]] = turno
            loop = False
        else:
            print("La casilla ya esta ocupada")
            os.system("pause")
            mostrar_tablero(tablero)


def mover_ficha(tablero: tuple, turno: int):
    nueva_posicion_ficha = {"fila": None, "columna": None}
    antigua_posicion_ficha = {"fila": None, "columna": None}
    loop = True
    while loop:
        posicion_valida = False
        while not posicion_valida:    
            print(f"Jugador {turno} - Introduzca la posicion de la ficha que quieres mover")
            antigua_posicion_ficha["fila"], antigua_posicion_ficha["columna"] = pedir_posicion()
            if tablero[antigua_posicion_ficha["fila"]][antigua_posicion_ficha["columna"]] == turno:
                if comprobar_movimiento(tablero, antigua_posicion_ficha["fila"], antigua_posicion_ficha["columna"]):
                    posicion_valida = True

                else:
                    print("La ficha no se puede mover")                    

            else:
                print("En esa posicion no hay ninguna ficha que puedas mover")
                os.system("pause")
                mostrar_tablero(tablero)            
        
        posicion_valida = False

        while not posicion_valida:
            print(f"Jugador {turno} - Introduzca la nueva posición para la ficha")
            nueva_posicion_ficha["fila"], nueva_posicion_ficha["columna"] = pedir_posicion()
            if (nueva_posicion_ficha["fila"], nueva_posicion_ficha["columna"]) in POSICIONES_POSIBLES[antigua_posicion_ficha["fila"]][antigua_posicion_ficha["columna"]]:    
                if tablero[nueva_posicion_ficha["fila"]][nueva_posicion_ficha["columna"]] == 0:
                    posicion_valida = True
                    loop = False
                    tablero[nueva_posicion_ficha["fila"]][nueva_posicion_ficha["columna"]] = turno
                    tablero[antigua_posicion_ficha["fila"]][antigua_posicion_ficha["columna"]] = 0                
                else:
                    print("La casilla ya esta ocupada.")
                    os.system("pause")
                    mostrar_tablero(tablero)

            else:
                print("No puedes mover la ficha a esa posición.")


def verificar_ganador(tablero, turno):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == turno or tablero[0][i] == tablero[1][i] == tablero[2][i] == turno:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == turno or tablero[0][2] == tablero[1][1] == tablero[2][0] == turno:
        return True

    else:
        return False


def jugar(tablero: tuple):
    ronda = 0
    turno = 0
    salir = False

    while not salir:
        mostrar_tablero(tablero)
        turno, ronda = cambiar_turno(turno, ronda)
        
        if ronda <= 3:
            colocar_ficha(tablero, turno, ronda)
        else:
            mover_ficha(tablero, turno)
        
        if verificar_ganador(tablero, turno) == True:
            mostrar_tablero(tablero)
            print(f"Jugador {turno} ha ganado")
            salir = True


def main():
    clear_console()
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)


if __name__ == "__main__":
    main()
