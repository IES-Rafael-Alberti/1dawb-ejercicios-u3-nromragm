import os

def clear_terminal():
    os.system("cls")

def lista_asignaturas(asignaturas):

    print(" - ".join(asignaturas))
    


def main():
    clear_terminal()
    
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
    
    lista_asignaturas(asignaturas)



if __name__ == "__main__":
    main()