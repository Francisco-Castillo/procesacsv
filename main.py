import csv
RUTA_ARCHIVO_CSV ="./resources/personas.csv"

with open(RUTA_ARCHIVO_CSV, encoding='latin1') as archivo:
    reader = csv.DictReader(archivo)
    personas = {}
    for linea in reader:
        jugador = linea["Jugador"]
        minutos = int(linea["Minutos"])
        if jugador in personas:
            personas[jugador]=personas[jugador] + minutos
        else:
            personas[jugador] = minutos
    print(personas)
