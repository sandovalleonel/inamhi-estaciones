import numpy as np

from obtener_datos.ConexionFtp import ConexionFtp
from obtener_datos.Rutas import Rutas
from procesar_datos.Umbral import Umbral
from procesar_datos.Estacion import Estacion
from procesar_datos.Procesamiento import Procesamiento

def parteUno():

    """obtener las Urls de todas las estaciones"""
    Urls = Rutas().obtenerUrls()# "/home/leonel/testAuto/M0003/D1/2020/10/15/"
    print(Urls)

    """obtener datos del servidor..."""
    objFtp = ConexionFtp("172.16.183.128", "leonel", "23456789")
    objFtp.conIniciar()
    objFtp.buscarArchivo(Urls[0])#recibe un string
    print(objFtp.fullPath)
    print(objFtp.data[:, 3])
    print(objFtp.info, "+++++++++")
    objFtp.conFinalizar()

    """limpiar la matriz obtenida del objeto ftp"""
    objEstacion = Estacion()
    objEstacion.Limpiar(objFtp.data)


    """leer archivo de umbrales"""
    objUmbral = Umbral(objFtp.fullPath)
    objUmbral.abrirArchivo()
    #print(objUmbral.matrizUmbral[:,3])




    """Realizar las operaciones con umbral y archivo obtenido de ftp"""
    objProcesamiento = Procesamiento(objEstacion.cabecera,objEstacion.datos,objUmbral.matrizUmbral)
    objProcesamiento.tamaArrays()
    print(objProcesamiento.listaFinal)


    """LLamar script guardar"""




def main():
    parteUno()



if __name__ == "__main__":
    main()
