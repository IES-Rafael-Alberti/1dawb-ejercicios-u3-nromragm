import os

FICHAS = (" ", "X", "O")

def clear_console():
    """Clears the console.

    In the os module if the Operating system is Windows 'os.name' will be 'nt', if the operating system is mac or linux-based it will be 'posix' 
    """
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
    
    for fila in tablero:
        print("-" * 13)
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


def colocar_ficha(tablero: tuple, turno: int):
    pos_ficha = {"fila": None, "columna": None}
    loop = True
    while loop:

        print(f"Jugador {turno}")

        pos_ficha["fila"],pos_ficha["columna"] = pedir_posicion()

        if tablero[pos_ficha["fila"]][pos_ficha["columna"]] == 0:
            tablero[pos_ficha["fila"]][pos_ficha["columna"]] = turno
            loop = False

        else:
            print("ERROR! Posicion no valida")
            os.system("pause")
        
        mostrar_tablero(tablero)


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
        turno, ronda = cambiar_turno(turno, ronda)
        colocar_ficha(tablero, turno)
        if verificar_ganador(tablero, turno):
            salir = True
            print(f"jugador {turno} ha ganado")

        elif ronda == 5:
            print("Empate")    
            salir = True


def main():
    clear_console()
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)
    

if __name__ == "__main__":
    main()