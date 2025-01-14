import requests
import sys

moduloActual = sys.modules[__name__]

ayuda = """
[SINTAXIS]
Fuzzineitor.py [opciones] [ruta del diccionario] [URL victima]

Ejemplo: Fuzzineitor.py -s RockYou https://github.com

[OPCIONES]
-h: Muestra este texto de ayuda

-s: Indica que quieres hacer fuzzing de subdominio, el texto del diccionario se añadira con un punto (.) al principio del dominio

-r: Indica que hacer fuzzing de ruta, el texto del diccionario se añadira con una barra (/) al final del dominio

-tp: Por defecto Fuzzineitor intentara conectarse por HTTPS, con este parametro indica que quieres conectarte con HTTP
"""

def subdominio(diccionario, dominio, protocolo):
    for line in diccionario:
        direccion = f"{protocolo}{line.strip()}.{dominio}"
        try:
            r = requests.get(direccion)
            print(f"[{direccion}] {r.status_code}")
        except requests.ConnectionError or requests.ConnectTimeout:
            print(f"[{direccion}] 404")

def ruta(diccionario, dominio, protocolo):
    for line in diccionario:
        direccion = f"{protocolo}{dominio}/{line.strip()}"
        r = requests.get(direccion)
        print(f"[{direccion}] {r.status_code}")

if __name__ == "__main__":

    numeroParametros = len(sys.argv)
    parametros = {
        "modo": None,
        "protocolo": "https://",
        "diccionario": sys.argv[numeroParametros - 2],
        "dominio": sys.argv[numeroParametros - 1]
    }

    if sys.argv[1] == "-h":
        print(ayuda)
        sys.exit(0)

    for i in range(1,numeroParametros):

        if sys.argv[i] == "-tp":
            parametros["protocolo"] = "http://"

        if sys.argv[i] == "-s":
            parametros["modo"] = "subdominio"


        if sys.argv[i] == "-r":
            parametros["modo"] = "ruta"


    if parametros["modo"] is None:
        print("Modo invalido")
        sys.exit(1)
    else:
        funcion = (getattr(moduloActual, parametros["modo"], None))
        funcion(diccionario=open(parametros["diccionario"], "r"), dominio=parametros["dominio"], protocolo=parametros["protocolo"])
sys.exit(0)