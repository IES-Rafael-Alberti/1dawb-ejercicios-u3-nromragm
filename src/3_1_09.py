def pedir_palabra():
    palabra = input("Introduce una palabra: ")
    return palabra

def vocal_en_palabra(palabra):
    a = 0
    i = 0
    e = 0
    o = 0
    u = 0

    for vocal in palabra:
        if vocal == "a":
            a += 1
        elif vocal == "o":
            o += 1
        elif vocal == "i":
            i += 1
        elif vocal == "u":
            u += 1
        elif vocal == "e":
            e += 1

    print(f"La palabra: {palabra} tiene {a} 'a', {e} 'e', {i} 'i', {o} 'o', {u} 'u'")        


def main():

    palabra = pedir_palabra()
    vocal_en_palabra(palabra)

                    
if __name__ == "__main__":
    main()
