precios = [10,4.5,11,20]
total_sin_iva = 0
total_con_iva = 0
contador = 0


for precio in precios:
    contador +=1

    while True:
        try:
            metros = input(f"cuantos metro quieres de tela {contador} ")
            metros = float(metros)
            total_sin_iva += (metros*precio)
            break
        
        except ValueError:
            print("Por favor, introduce un número válido con numeros")
            

total_con_iva=total_sin_iva*1.21

print(f"\nel total sin iva serían : {total_sin_iva}\n y el total con iva serían : {total_con_iva}")

