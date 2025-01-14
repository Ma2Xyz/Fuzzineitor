import requests
import sys

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
        print(help)
        sys.exit(0)

    if sys.argv[1] == "-s":
        subdominio(open("diccionarios/" + sys.argv[2], "r"), sys.argv[3])

    if sys.argv[1] == "-r":
        ruta(open("diccionarios/" + sys.argv[2], "r"), sys.argv[3])
sys.exit(0)