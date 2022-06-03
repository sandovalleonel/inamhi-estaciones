import os
import time
import numpy as np
class ListaArchivo:

   def imprimirArchivos(self, ruta):
       print(ruta)
       with os.scandir(ruta) as ficheros:
           for fichero in ficheros:

               #print(fichero.name)
               time.sleep(0.01)
               rutaCompleta = (ruta+"/"+fichero.name)
               self.usarNumpy(rutaCompleta)

   def usarNumpy(self,fullPath):
       try:
           File_data = np.loadtxt(fullPath, dtype="str", delimiter=",")
           cabecera = File_data[0, :]
           datos = File_data[1:, 1:]

           datos = np.char.strip(datos)
           datos[datos == "//////"] = np.nan;
           datos[datos == "/////"] = np.nan;
           datos = datos.astype(float)
           datos = np.mean(datos, axis=0)
           datos = np.mean(datos)
           #print(datos)


       except:
           print()
           #print("error archivo: "+fullPath)




