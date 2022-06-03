import time
from obtener_datos.ConexionFtp import ConexionFtp
from obtener_datos.Rutas import Rutas
from procesar_datos.Umbral import Umbral
from procesar_datos.Estacion import Estacion
from procesar_datos.Procesamiento import Procesamiento
from guardar_datos.ConnPostgres import ingresarPostgresUno, consultarDatos, ingresarPostgresMuchos
from guardar_datos.GuardarDatosPrecesados import guardar

def parteUno():

    tInicio = time.time()

    """obtener las Urls de todas las estaciones"""
    #Urls = Rutas().obtenerUrls()# "/home/leonel/testAuto/M0003/D1/2020/10/15/"
    Urls = Rutas().rutasQuemada()
    print(Urls)

    """obtener datos del servidor..."""
    objFtp = ConexionFtp("192.168.1.18", "leonel", "23456789")
    objFtp.conIniciar()

    objFtp.buscarArchivo(Urls[0])#recibe un string
    print(objFtp.fullPath)
    #print(objFtp.data[:, 3])
    #print(objFtp.info, "")
    objFtp.conFinalizar()

    """limpiar la matriz obtenida del objeto ftp"""
    objEstacion = Estacion()
    objEstacion.Limpiar(objFtp.data)


    """leer archivo de umbrales"""
    objUmbral = Umbral(objFtp.fullPath)
    objUmbral.abrirArchivo()
    #print(objUmbral.matrizUmbral[:,3])

    """
    cambio...si se sale del umbral...poner datos null
    la salida final para guardar poner adicionalmente cuantos valores se usaron para sumaro promediar...buscar en la columna
    8_544161m para ver si sirve o no la fila..para eliminar
    """


    """Realizar las operaciones con umbral y archivo obtenido de ftp"""
    objProcesamiento = Procesamiento(objEstacion.cabecera,objEstacion.datos,objUmbral.matrizUmbral)
    objProcesamiento.tamaArrays()
    #print(objProcesamiento.listaFinal)

    """LLamar script guardar"""

    ingresarPostgresMuchos(guardar(objProcesamiento.listaFinal))

    #consultarDatos("select * from Administrativo.provincias")

    tFin = time.time()
    tTotal = tFin-tInicio

    print("Tiempo total " + str(tTotal))




def main():
    parteUno()



if __name__ == "__main__":
    main()
