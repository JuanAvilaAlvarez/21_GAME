from random import randint

#Generación del mazo
figuras = ["pica", "diamante", "trebol", "corazon"]
numeros = ["A", "J", "Q", "K"] + [str(i) for i in range (2,11)]
mazo = [(a,b) for a in figuras for b in numeros]

c = 0

def nueva_carta(lugar):
    global c
    n = randint(0,(51-c))
    if lugar == "casa":
        casa.append(mazo[n])
    elif lugar == "juego":
        juego.append(mazo[n])
    global numero
    numero = mazo[n][1]
    mazo.remove(mazo[n])
    c += 1
    return numero

def sumar(numero):
    if numero in ["J", "Q", "K"]:
        return 10
    elif numero == "A":
        return 1
    else:
        return numero

#Casa
casa = []
contador_casa = 0
while c < 2:
    nueva_carta("casa")
    contador_casa += int(sumar(numero))

print(f"El mazo de la casa tiene un {casa[0]}")

#Juego
juego = []
contador = 0
while c < 4:
    nueva_carta("juego")
    contador += int(sumar(numero))

print(f"Tu juego es: {juego}")
continuar = input("¿Deseas continuar?(si/no): ")

if continuar == "si":
    while True:
        nueva_carta("juego")
        contador += int(sumar(numero))
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
            nueva_carta("casa")
            contador_casa += int(sumar(numero))
        elif contador_casa > 21:
            print(f"Le has ganado a la casa, esta tiene un puntaje de {contador_casa} y tu tienes un puntaje de {contador}")
            break
        elif contador_casa >= contador & contador_casa < 21:
            print(f"La casa te ha ganado, esta tiene un puntaje de {contador_casa} y tu tienes un puntaje de {contador}")
            break