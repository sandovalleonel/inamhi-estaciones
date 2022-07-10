from multiprocessing import Pool
import time
from obtener_datos.ConexionFtp import ConexionFtp
from obtener_datos.Rutas import Rutas
from procesar_datos.Umbral import Umbral
from procesar_datos.Estacion import Estacion
from procesar_datos.Procesamiento import Procesamiento
from guardar_datos.GuardarDatosPrecesados import guardar

def Paraleliszar():
    tIn = time.time()
    # Urls = Rutas().obtenerUrls()# "/home/leonel/testAuto/M0003/D1/2020/10/15/"
    Urls = Rutas().rutasQuemada()
    #print(Urls)

    with Pool(5) as p:
        p.map(cagarProcesos,Urls)
    tFi = time.time()
    tTott = tFi - tIn
    print("Tiempo final Completo  "+str((tTott  )))




def cagarProcesos(Url):

    #print("*"*40)
    

    """obtener datos del servidor..."""
    objFtp = ConexionFtp("localhost", "leonel", "23456789")
    objFtp.conIniciar()

    objFtp.buscarArchivo(Url)#recibe un string
    print(objFtp.fullPath)


    """limpiar la matriz obtenida del objeto ftp"""
    objEstacion = Estacion()
    objEstacion.Limpiar(objFtp.data)

    """leer archivo de umbrales"""
    objUmbral = Umbral(objFtp.fullPath)
    objUmbral.abrirArchivo()

    """Realizar las operaciones con umbral y archivo obtenido de ftp"""
    objProcesamiento = Procesamiento(objEstacion.cabecera,objEstacion.datos,objUmbral.matrizUmbral)
    objProcesamiento.tamaArrays()
    #print(objProcesamiento.listaFinal)
    #funcionTemporal(objProcesamiento.listaFinal)
    """LLamar script guardar"""
    tIn = time.time()
    guardar(objProcesamiento.listaFinal, objUmbral.nombreArchivoUmbral,objFtp.fullPath)
    tFi = time.time()
    tTott = tFi - tIn
    print("Tiempo save Completo  "+str((tTott  )))




def funcionTemporal(array):
    cont=1
    for fila in array:
        print(fila)
        if fila[2] != 0:
            #print(fila[1])
            cont=cont+1
    
   