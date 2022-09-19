armas = ("Espada", "Hacha", "Maza", "Sartén")
armaduras = ("Camisa", "Chaqueta de Piel", "Cota de malla", "Coraza")
equipamiento = ["1", "2", "3"]
stats = ("Fuerza", "Defensa", "Suerte")
statsValue = {"Fuerza": 10, "Defensa": 10, "Suerte": 10}

# Selección de armas
while input("¿Quieres ver las armas? ") != "no":
    print("¿Qué arma quieres ver?")
    
    verArma = input()
    
    if verArma == "espada":
        print("La espada te da +1 a Fuerza y +1 a defensa.")
        print("Quieres equipar la espada?")
        quieres = input()
        if quieres == "si":
            print("Enhorabuena, has equipado la espada!. Recuerda que solo puedes llevar un arma a la vez")
            equipamiento.insert(0, "espada")
        else:
            print("Sigue mirando")
    
    if verArma == "hacha":
        print("El hacha te da +3 a Fuerza y -1 a defensa.")
        print("Quieres equipar el hacha?")
        quieres = input()
        if quieres == "si":
            print("Enhorabuena, has equipado el hacha!. Recuerda que solo puedes llevar un arma a la vez")
            equipamiento.insert(0, "hacha")
        else:
            print("Sigue mirando")
    
print("cierras el armario y notas el peso de tu " + str(equipamiento[0]) + " en tu mano... estas listo")            
    
