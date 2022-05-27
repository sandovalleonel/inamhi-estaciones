import psycopg2
import json
import pathlib


rutaJson = pathlib.Path(__file__).parent.absolute()

conexion = None
with open(str(rutaJson)+"/credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)
try:
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)