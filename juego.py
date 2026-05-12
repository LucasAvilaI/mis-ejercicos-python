import random
secreto= random.randint(0,20)
intento=0

print("REGLAS DEL JUEGO\n1.Tienes que adivinar el numero que estoy pensando en 5 intentos\n2.Te diré si no aciertas si el numeor es mayor o menor que el tuyo\n\n¡VAMOS ALLA!")

while intento<5:
    numero=int(input("¿Que numero estoy pensando?" ))
    if secreto==numero:
        print("¡Has acertado!")
        break
    else:
        if secreto<numero:
            print("¡Has fallado! El numero que estoy pensando es menor.")
            intento +=1
        else:
            print("¡Has fallado! El numero que estoy pensando es mayor.")
            intento +=1
    print(f"te quedan {5 -intento} intentos")
    
if secreto != numero:
    print("Has perdido")
