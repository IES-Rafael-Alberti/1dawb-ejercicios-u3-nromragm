def eliminar_multiplos_de_tres(abcedario):
    del abcedario[2::3]
    
    return abcedario


def main():

    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


    print(eliminar_multiplos_de_tres(abecedario))

 

if __name__ == "__main__":
    main()
