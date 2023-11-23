def contar_vocales(palabra):

    recuento_vocales = [0, 0, 0, 0, 0]


    palabra = palabra.lower()

    for caracter in palabra:

        if caracter in "aeiou":

            indice_vocal = "aeiou".index(caracter)
            recuento_vocales[indice_vocal] += 1


    vocales = "aeiou"
    for i in range(len(vocales)):
        print(f"La vocal {vocales[i]} aparece {recuento_vocales[i]} veces en la palabra.")

def main():

    palabra_usuario = input("Introduce una palabra: ")
    
    contar_vocales(palabra_usuario)

if __name__ == "__main__":
    main()
