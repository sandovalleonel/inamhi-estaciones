"""
Cargar el archivo con los umbrales respectivos al archivo
Entrada
    url completa con el nombre del archivo
Salida
    array numpy
"""
import numpy as np
class Umbral:
    matrizUmbral = None
    nombreArchivoUmbral = None
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo


    def rutaUmbral(self):
        tam = len(self.nombreArchivo.split("/"))
        auxNombre = self.nombreArchivo.split("/")[tam - 1]
        nombre = auxNombre.split("_")[0] + "_" + auxNombre.split("_")[1] + ".rep"
        self.nombreArchivoUmbral = nombre

        return "dataUmbral/" + nombre



    def abrirArchivo(self):

        try:
            mat = np.loadtxt(self.rutaUmbral(),dtype="str", delimiter=",")

            self.matrizUmbral = mat[3:,1:].astype(float)#ver los datos que son importantes
            if self.matrizUmbral.shape[0] < 2 or self.matrizUmbral.shape[1] < 5:
                print("Error archivo no valido 'columnas minimas'-- Umbral.py")

        except FileNotFoundError as e:
            print("Error archivo no encontrado ..no exite archivo del umbral, o no tiene formato correcto")
        except:
            print("Error cargar archivo umbral")



