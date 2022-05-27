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
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo


    def rutaUmbral(self):
        tam = len(self.nombreArchivo.split("/"))
        auxNombre = self.nombreArchivo.split("/")[tam - 1]
        nombre = auxNombre.split("_")[0] + "_" + auxNombre.split("_")[1] + ".rep"

        return "dataUmbral/" + nombre



    def abrirArchivo(self):
        try:
            self.matrizUmbral = np.loadtxt(self.rutaUmbral(),dtype="str", delimiter=",")
        except FileNotFoundError as e:
            exit("Error archivo no encontrado ..no exite archivo del umbral")


