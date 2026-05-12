temperatura = float(input("¿que temperatura hace hoy?"))
lluvia=input("¿Llueve?").lower().strip()
ocasion=input("¿Que ocasión es (formal,casual,deporte...)?\n").lower().strip()

afirmaciones = ["si", "Si", "mucho", "quizas", "bastante"]
negaciones=["no","Para nada","no creo","no tiene pinta","nada"]
formal=["formal","elegante","serio","seria"]
deporte=["deporte","sport"]
casual=["casual","relajado","tranquilo"]

    
if lluvia in afirmaciones:
    estado_lluvia="si"
elif lluvia in negaciones:
    estado_lluvia="no"
else:
    estado_lluvia="dudoso"

print(f"\nTemperatura: {temperatura} \nLluvia: {estado_lluvia} \nOcasion: {ocasion}\nTe recomiendo lo siguiente:\n")

if ocasion in formal:
    print("Ponte elegante. Una camisa por ejemplo")
elif ocasion in casual:
    print("No hace falta ir elegante. Mejor una sudadera o jeans")
elif ocasion in deporte:
    print("Ponte comodo, te vas a mover. Un chandal y deportivas")
else:
    print("Ante la duda, ponte un polo claro, vaqueros y unos zapatos normales. seguro que aciertas")



if temperatura<=15:
    if temperatura<=10 and estado_lluvia=="si":
        print("Abrigate mucho y lleva paraguas")
    elif temperatura<=10 and estado_lluvia=="no":
        print("Abrigate mucho")
    else:
        print("Lleva una chaqueta")
elif temperatura >=30:
    print("Lleva ropa ligera y bloqueador solar")
else:
    print("No necesitas una chaqueta.")

if lluvia == "si" and temperatura>10:
    print("Lleva paraguas tambien.")
elif lluvia == "no":
    print("No te hace fata paraguas.")

