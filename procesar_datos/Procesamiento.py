"""
Trabajar con las matrices limpiadas del de umbral y estacion,
guardar los datos en un array la columna y el dato resultante y llamar a la coneccion potgres...
la case debe retornar el array-----
"""

class Procesamiento:
    def __init__(self, cabecera,datos,umbral):
        self.cabecera = cabecera
        self.datos = datos
        self.umbral = umbral

    def tamaArrays(self):
        print(self.cabecera.shape)
        print(self.datos.shape)
        print(self.umbral.shape)
        print(self.cabecera[5])
        #########3
        validaRangos = lambda x: x if (x > 1.1 and x < 6.1) else 9999

        ia = -3
        for i in range(-4,20):
            print(validaRangos(ia))
            ia = ia + 0.4
