from random import randint

#Generación del mazo
figuras = ["pica", "diamante", "trebol", "corazon"]
numeros = ["A", "J", "Q", "K"] + [str(i) for i in range (2,11)]
mazo = [(a,b) for a in figuras for b in numeros]

c = 0

#Casa
casa = []
contador_casa = 0
while c < 2:
    n = randint(0,(51-c))
    casa.append(mazo[n])
    if mazo[n][1] in ["A", "J", "Q", "K"]:
        contador_casa += 10
    else:
        contador_casa += int(mazo[n][1])
    mazo.remove(mazo[n])
    c += 1

print(f"El mazo de la casa tiene un {casa[0]}")

#Juego
juego = []
contador = 0
while c < 4:
    n = randint(0,(51-c))
    juego.append(mazo[n])
    if mazo[n][1] in ["A", "J", "Q", "K"]:
       contador += 10
    else:
       contador += int(mazo[n][1])
    mazo.remove(mazo[n])
    c += 1

print(f"Tu juego es: {juego}")
continuar = input("¿Deseas continuar?(si/no): ")

if continuar == "si":
    while True:
        n = randint(0,(51-c))
        juego.append(mazo[n])
        if mazo[n][1] in ["A", "J", "Q", "K"]:
            contador += 10
        else:
            contador += int(mazo[n][1])
        mazo.remove(mazo[n])
        c += 1
        if contador > 21:
            print(f"Te has pasado, tu puntaje actual es de: {contador}")
            break
        else: 
            print(f"Tu juego es: {juego}")
            continuar = input("¿Deseas continuar?(si/no): ")
            if continuar == "no":
                break

if continuar != "si":
    while True:
        if contador_casa < contador:
            n = randint(0,(51-c))
            casa.append(mazo[n])
            if mazo[n][1] in ["A", "J", "Q", "K"]:
                contador_casa += 10
            else:
                contador_casa += int(mazo[n][1])
            print(mazo[n])
            mazo.remove(mazo[n])
            c += 1
        elif contador_casa > 21:
            print(f"Le has ganado a la casa, esta tiene un puntaje de {contador_casa} y tu tienes un puntaje de {contador}")
            break
        elif contador_casa >= contador & contador_casa < 21:
            print(f"La casa te ha ganado, esta tiene un puntaje de {contador_casa} y tu tienes un puntaje de {contador}")
            break