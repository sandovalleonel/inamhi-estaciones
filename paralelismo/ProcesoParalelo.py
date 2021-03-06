from multiprocessing import Pool
from ntpath import join
import time
from obtener_datos.ConexionFtp import ConexionFtp
from obtener_datos.Rutas import Rutas
from procesar_datos.Umbral import Umbral
from procesar_datos.Estacion import Estacion
from procesar_datos.Procesamiento import Procesamiento
from guardar_datos.GuardarDatosPrecesados import guardar

modulo2 =[]
modulo3 =[]
modulo4 =[]
modulo1 =[]

def Paraleliszar():

    metricasTiempo = []

    tIn = time.time()
    # Urls = Rutas().obtenerUrls()# "/home/leonel/testAuto/M0003/D1/2020/10/15/"
    Urls = Rutas().rutasQuemada()

    with Pool(15) as p:
        metricasTiempo = ( p.map(cagarProcesos,Urls))
    tFi = time.time()
    tTott = tFi - tIn
    print("Tiempo final Completo  "+str((tTott  )))

    escribirFichero(metricasTiempo)




def cagarProcesos(Url):

    """obtener datos del servidor..."""
    tInmod1 = time.time()
    objFtp = ConexionFtp("localhost", "leonel", "23456789")
    objFtp.conIniciar()
    objFtp.buscarArchivo(Url)#recibe un string
    print(objFtp.fullPath)
    tFimod1 = time.time()
    tTottmod1 = tFimod1 - tInmod1
    
    
    


    """limpiar la matriz obtenida del objeto ftp"""
    tInmod2 = time.time()
    objEstacion = Estacion()
    objEstacion.Limpiar(objFtp.data)
    
    """leer archivo de umbrales"""
    objUmbral = Umbral(objFtp.fullPath)
    objUmbral.abrirArchivo()
    
    """Realizar las operaciones con umbral y archivo obtenido de ftp"""
    objProcesamiento = Procesamiento(objEstacion.cabecera,objEstacion.datos,objUmbral.matrizUmbral)
    objProcesamiento.tamaArrays()
    tFimod2 = time.time()
    tTottmod2 = tFimod2 - tInmod2
    


    """LLamar script guardar"""
    tInmod3 = time.time()
    guardar(objProcesamiento.listaFinal, objUmbral.nombreArchivoUmbral,objFtp.fullPath)
    tFimod3 = time.time()
    tTottmod3 = tFimod3 - tInmod3
    
    return [tTottmod1,tTottmod2,tTottmod3]


def escribirFichero(matriz):
    file = open("temp/tiempo.txt", "w")
    aux=0
    for linea in matriz:
        aux+=sum(linea)
        fila =str(linea[0])+","+str(linea[1])+","+str(linea[2])+"\n"
        
        file.write(fila)
    file.close()
    print(aux)
