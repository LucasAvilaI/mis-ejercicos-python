saldo=1000.00
sacar=1
ingresar=2
salir=3
continuar=True

while continuar==True:
    accion=float(input("¿Que accion desea realizar ahora?\n PARA RETIRAR PULSE 1\n PARA INGRESAR PULSE 2\n PARA SALIR PULSE 3\n"))
    if accion==1:
        salida= float(input("¿Cuanto dinero desea retirar?"))
        if saldo-salida<0:
            print("Disculpa, no tienes saldo suficiente\n\n")
        else:
            saldo = saldo-salida
            print(f"Su saldo actual es de {saldo}€\n\n")
    elif accion == 2:
        ingreso= float(input("¿Cuanto dinero desea ingresar?"))
        saldo = saldo + ingreso
        print(f"Su saldo actual es de {saldo}€\n\n")
    elif accion == 3:
        continuar=False
    else:
        print("No le hemos entendido bien. Porfavor siga las intrucciones correctamente:\n\n")

print("¿Muchas gracias!¡Le deseamos un feliz dia!")


        
            