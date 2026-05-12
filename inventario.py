inventario = {
    "espada":2,"pocion":4,"flecha":3
}


def ver_inventario():
    print("Contenido de la mochila:")
    for objeto,cantidad in inventario.items():
        print(f"- {objeto},{cantidad}")


while True:
    respuesta=input("\n\n¿que quiere hacer?\n Pulsa 1 para ver el inventario \n Pulsa 2 para añadir objeto\n Pulsa 3 para ver eliminar objeto\n Pulsa 4 para ver salir\n") # Añade los paréntesis para que funcione
    if respuesta == "1":
        ver_inventario()
    elif respuesta == "2":
        entrada=input("Escribe lo que quieras añadir:")
        if entrada in inventario:
            inventario[f"{entrada}"]+=1
        else:
            inventario[f"{entrada}"]=1
        print(f"{entrada} ha sido añadido")
    elif respuesta == "3":
        salida=input("Escribe lo que quieras quitar:")
        if salida in inventario:
            inventario[f"{salida}"]-=1
            print(f"{salida} ha sido eliminada")
        else:
            print("Creo que lo que has escrito no se encuentra en la lista, te lo refresco:")
            ver_inventario()
    elif respuesta == "4":
        print("Gracias")
        break
    else:
        print("opcion no valida intentelo de nuevo")






