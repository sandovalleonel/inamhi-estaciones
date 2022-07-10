import os
import re
import numpy as np
from io import BytesIO
from ftplib import FTP
"""
Entradas 
    host
    user
    password
    rutas de estaciones
Salidas
    ruta completa incluido nombre del fichero
    array numpy del fichero
    numero de filas y columnas del array numpy    
"""


class ConexionFtp:
    ftp = None
    fullPath = []
    data = []
    info = []
    rutaDestino = "data"

    def __init__(self, host, usuario, contrasenia):
        self.host = host
        self.usuario = usuario
        self.contrasenia = contrasenia
        #print("inicalizacion ftp")


    def conIniciar(self):
        #print(os.path.dirname(os.path.realpath(__file__)))#ruta real

        self.ftp = FTP(self.host)  # connect to host, default port
        self.ftp.login(self.usuario,self.contrasenia)  # user anonymous, passwd anonymous@
        self.ftp.encoding = "utf-8"


    def conFinalizar(self):
        self.ftp.quit()

    def crearDirectorio(self):
        nombreCarpeta = self.rutaDestino
        if not os.path.exists(nombreCarpeta):
            os.makedirs(nombreCarpeta)

    def buscarArchivo(self,Url):

        self.ftp.cwd(Url)   #controlar que la carpeta exista
        files = self.ftp.nlst()

        filesFiltrados= self.listFiles(Url, files)

        if len(filesFiltrados) == 0:
            exit("carpeta sin archivos ")

        self.fullPath = filesFiltrados[len(filesFiltrados)-1] # verificar si es el ultimo archivo
        self.cargarArchivoEnMemoria(self.fullPath)
        #self.descargarArchivo(self.fullPath)
        self.conFinalizar()

    def descargarArchivo(self,RutaCompleta):
        self.crearDirectorio()
        nombreArchivo  = RutaCompleta.split("/")
        nombreArchivo = (nombreArchivo[len(nombreArchivo)-1])
        self.ftp.retrbinary("RETR "+RutaCompleta, open("data/"+nombreArchivo, 'wb').write)

    def cargarArchivoEnMemoria(self,RutaCompleta):
        r = BytesIO()
        self.ftp.retrbinary('RETR '+RutaCompleta, r.write)
        valoresEstacion = r.getvalue().decode('UTF-8').replace('\r', '')

        valoresEstacionFilas = valoresEstacion.split("\n")
        arrayEstacion = []
        for valoresEstacionColumnas in valoresEstacionFilas:
            if len(valoresEstacionColumnas.split(",")) > 1:
                arrayEstacion.append(valoresEstacionColumnas.split(","))

        dataAux = np.array(arrayEstacion,dtype=str)
        self.data = dataAux
        self.info = dataAux.shape





    def listFiles(self,Url,files, patern='\.rep$'):
        matchedFiles = []
        for filename in files:
            if re.search(patern, filename):
                matchedFiles.append(Url+filename)
        return matchedFiles


"""
#Ejemplo
obj = ConexionFtp("172.16.183.128","leonel","23456789")
obj.conIniciar()
Url = "/home/leonel/testAuto/M0003/D1/2020/10/15/"
obj.buscarArchivo(Url)
print(Url)
print(obj.fullPath)
print(obj.data)
print(obj.info)
obj.conFinalizar()
"""






