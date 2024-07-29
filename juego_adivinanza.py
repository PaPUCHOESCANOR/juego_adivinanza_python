import random
from re import T


numero_secreto = random.randint(0,100)
adivinado = False
cant_intentos= 0
max_intentos = 5 
print("bienvenido al juego del numero secreto")
while not adivinado and cant_intentos < max_intentos:
    numero = int(input("introduce un numero del 1 al 99 ")) 
    if numero == numero_secreto:
        print("felicidades has adivinado el numero secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("el nuemro es mayor al ingresado")
    else:
        print("el numero es menor al ingresado ")
    cant_intentos += 1
if not  cant_intentos < max_intentos:
    print("game over")