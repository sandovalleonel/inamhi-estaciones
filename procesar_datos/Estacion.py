"""
Recibe un array numpy y proceder a verficar si tienes las columnas necesarias
y remplazar los caracteres , finalmente convertir el array en float
"""
from obtener_datos.ConexionFtp import ConexionFtp
import numpy as np
class Estacion:
    datos = None
    cabecera = None
    def Limpiar(self,data):

        if data.shape[0] < 2  or data.shape[1] < 5:
            exit("Erro archivo no valido -- Estaciones.py")

        self.cabecera = data[0, :]
        datosTemp = data[1:, 1:]

        datosTemp = np.char.strip(datosTemp)
        datosTemp[datosTemp == "//////"] = np.nan
        datosTemp[datosTemp == "/////"] = np.nan
        self.datos = datosTemp.astype(float)
        print(self.datos.shape)


"""
obj = ConexionFtp("172.16.183.128","leonel","23456789")
obj.conIniciar()
Url = "/home/leonel/testAuto/M0003/D1/2020/10/15/"
obj.buscarArchivo(Url)

obj.conFinalizar()

objEstacion = Estacion()
objEstacion.Limpiar(obj.data)
print(np.mean(objEstacion.datos[:,84]))
print(objEstacion.cabecera[85])
"""



