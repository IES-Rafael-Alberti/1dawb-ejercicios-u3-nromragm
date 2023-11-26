def main():

    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}

    frutas_comunes = set_frutas1 & set_frutas2
    print("Frutas comunes: ", frutas_comunes)
    
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    print("Frutas que están en frutas1 pero no en frutas2: ", frutas_solo_en_frutas1)  
    
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    print("Frutas que están en frutas2 pero no en frutas1: ", frutas_solo_en_frutas2)


if __name__ == "__main__":
    main()