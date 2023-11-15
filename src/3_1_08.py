def palindromo(palabra):
    salir = True
    cont1 = 0
    cont2 = -1
    palindromo = True
    while salir and cont1 < len(palabra) / 2:
        if palabra [cont1] != palabra [cont2]:
            salir = False 
            palindromo = False

        cont1 += 1
        cont2 -= 1
    
    return palindromo


def main():

    palabra = input("Introduce una palabra: ")
    palabra = list(palabra)
    if palindromo(palabra) == True:
        print(f"{palabra} es un palindromo")

    else:
        print(f"{palabra} no es un palindromo")    
        
                    
if __name__ == "__main__":
    main()
