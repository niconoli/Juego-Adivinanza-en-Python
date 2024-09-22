import random

numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("¡Bienvenido al juego de adivinar el numero secreto!")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Introduce un número del 1 al 99: ")  # TODO: convertir a numero
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicitaciones, has adivinado el numero secreto!")
        adivinado = True
        break
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    
    cant_intentos +=1
    if cant_max_intentos - cant_intentos == 0:
        pass
    else:
        print("Te quedan",cant_max_intentos - cant_intentos, "Intentos")

if not cant_intentos < cant_max_intentos:
    print("¡GAME OVER! Te quedaste sin intentos, el numero era", numero_secreto)
