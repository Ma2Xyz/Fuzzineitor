import requests
import sys

ayuda = """
[SINTAXIS]
Fuzzineitor.py [opciones] [ruta del diccionario] [URL victima]

Ejemplo: Fuzzineitor.py -s RockYou https://github.com

[OPCIONES]
-s: Indica que quieres hacer fuzzing de subdominio, el texto del diccionario se añadira con un punto (.) al principio del dominio

-r: Indica que hacer fuzzing de ruta, el texto del diccionario se añadira con una barra (/) al final del dominio
"""

def subdominio(diccionario, dominio):
    for line in diccionario:
        direccion = dominio.replace("://", f"://{line.strip()}.")
        try:
            r = requests.get(direccion)
            print(f"[{direccion}] {r.status_code}")
        except requests.ConnectionError or requests.ConnectTimeout:
            print(f"[{direccion}] 404")

def ruta(diccionario, dominio):
    for line in diccionario:
        direccion = f"{dominio}/{line.strip()}"
        r = requests.get(direccion)
        print(f"[{direccion}] {r.status_code}")

if __name__ == "__main__":

    if sys.argv[1] == "-h":
        print(ayuda)
        sys.exit(0)

    if sys.argv[1] == "-s":
        subdominio(open(sys.argv[2], "r"), sys.argv[3])

    if sys.argv[1] == "-r":
        ruta(open(sys.argv[2], "r"), sys.argv[3])
sys.exit(0)