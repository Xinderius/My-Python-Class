meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL":"Una respuesta a una broma",
            "SHEESH":"Ligera desaprobacion",
            "CREEPY":"Aterrador, Siniestro",
            "AGGRO":"Ponerse agresivo/enojado",
            "XD":"Es como el LOL, es algo gracioso",
            "F":"Es como decir lo siento",
            "GG":"Decir buen juego",
            "MB":"Es decir mi error",
            }

for i in range(5):
    word = input("HEY, HOLA, Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print("El significado de la palabra es: ", meme_dict[word])
    else:
            # ¿Qué hacer si no se encuentra la palabra?
            print("No se cual sea el significado")
