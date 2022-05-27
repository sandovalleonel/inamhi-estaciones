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


class Procesamiento:
    listaFinal = []
    def __init__(self, cabecera,datos,umbral):
        self.cabecera = cabecera
        self.datos = datos
        self.umbral = umbral

    def tamaArrays(self):
        print("*"*40)
        #print(self.cabecera.shape)
        print(self.datos.shape)
        #print(self.umbral.shape)
        #########

        ###eliminar filas con banderas
        neww = np.delete(self.datos, [1,2,3,4], axis=0) ##eliminar datos no relevantes
        print(neww.shape)
        ###eliminar filas con banderas


        for i in range(self.umbral.shape[1]):
            indice = i * 2
            arr = self.datos[:,indice]
            umbralMaximo = self.umbral[2,i]
            umbralMinimo = self.umbral[3,i]
            valorRemplazo = self.umbral[4,i]
            lista_nueva = list(map(lambda x: x if (x > umbralMinimo and x < umbralMaximo) else valorRemplazo, arr))
            #print(lista_nueva)

            ##sumar o promediar
            cabeceraNombre = self.cabecera[indice]#.split("_")[1]
            if(self.umbral[1,i] == 1):
                res = (sum(lista_nueva))
                self.listaFinal.append([cabeceraNombre,res])

            elif(self.umbral[1,i] == 0):
                res = (sum(lista_nueva)/len(lista_nueva))
                self.listaFinal.append([cabeceraNombre, res])
