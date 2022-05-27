import os
from datetime import datetime
"""
Entradas
    Ruta completa del archivo con el nombre de las estaciones
Salidas
    lista de urls
"""

class Rutas:
    nombreArchivo = "estaciones/nombres.txt"
    def obtenerFecha(self):
        return (datetime.today().strftime('%Y/%m/%d'))


    def obtenerUrls(self):
        listaRutas = []
        fecha = self.obtenerFecha()

        file = open(self.nombreArchivo, 'r')
        for linea in file:
            #listaRutas.append(linea.strip()+fecha)
            listaRutas.append(linea.strip() + "2020/10/15/")
        file.close()

        return (listaRutas)
