"""
Trabajar con las matrices limpiadas del de umbral y estacion,
guardar los datos en un array la columna y el dato resultante y llamar a la coneccion potgres...
la case debe retornar el array-----
Etradas
    numpy array adatos
    numpy array cabeceras
    numpy array umbral
"""
import numpy as np
from numpy.core._multiarray_umath import error


class Procesamiento:
    listaFinal = []
    def __init__(self, cabecera,datos,umbral):
        self.cabecera = cabecera
        self.datos = datos
        self.umbral = umbral

    def filaMantenimiento(self):


        #buscar pos columna manteniemiento
        posColumna = -1
        i = 0

        for val in self.cabecera:
            if val.split("_")[1] == '544161m':
                posColumna = i
                break
            i = i+1

        if(posColumna != -1):
            #ver que columnas se deben eliminar
            auxColumnaMantenimiento = self.datos[:,posColumna]
            lista = np.where(auxColumnaMantenimiento == 1 )

            ###eliminar filas con banderas
            if(len(lista[0]) > 0):
                neww = np.delete(self.datos, lista[0], axis=0) ##eliminar datos no relevantes
                self.datos = neww


    def tamaArrays(self):
        self.listaFinal = []

        try:

            self.filaMantenimiento()
            #print("*"*40)
            if self.datos.shape[1] != self.umbral.shape[1]:
                exit("error el archivo umbral y matriz de datos no tiene mismo numero de columnas")

            for i in range(self.datos.shape[1]):

                arr = self.datos[:,i]
                umbralMaximo = self.umbral[1,i]
                umbralMinimo = self.umbral[2,i]

                lista_nueva = list(map(lambda x: x if (umbralMinimo <= x <= umbralMaximo) else None , arr))
                lista_nueva = list(filter(None, lista_nueva))


                ##sumar o promediar
                cabeceraNombre = self.cabecera[i]#.split("_")[1]

                #suma
                if(self.umbral[0,i] == 1):
                    res = (sum(lista_nueva))
                    self.listaFinal.append([cabeceraNombre,res,len(lista_nueva)])
                #promedio
                elif(self.umbral[0,i] == 0):
                    res = 0
                    if len(lista_nueva) != 0:
                        res = (sum(lista_nueva)/len(lista_nueva))
                    self.listaFinal.append([cabeceraNombre, res,len(lista_nueva)])


        except error:
            CRED = '\033[91m'
            CEND = '\033[0m'
            print(CRED + "Error procesar archivo procesamiento.py seccion preprocesamiento ..............ya no procesados, salto alsiguiente archivo "+CEND)