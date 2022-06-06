import numpy as np

list = ['../dataUmbral/M0024_D1.rep',
        '../dataUmbral/M1107_D1.rep',
        '../dataUmbral/M5090_D1.rep']
caberceraTotal = []

def convertirTablas(nombreEstacion,lista):
    for nombre in lista:
        auxNombre = "test." + nombreEstacion + "_D1_" + nombre
        caberceraTotal.append(auxNombre)

def escribirFichero(lista):
    with open('tablas.sql', 'w') as f:
        for tabla in lista:
            f.write(tabla)

for nombre in list:
    fichero = np.loadtxt(nombre,dtype="str",delimiter=",")
    cabeceras = fichero[1,1:]
    nombreEstacion = fichero[1,0]
    convertirTablas(nombreEstacion,cabeceras)

#crear script para las tablas

listaEscribir = []
for Tabla in caberceraTotal:
    nombreTabla = (f"""
        CREATE TABLE IF NOT EXISTS {Tabla}(
               id SERIAL PRIMARY KEY,
               fecha_creacion date,
               
               
               nom VARCHAR NOT NULL,
               res VARCHAR NOT NULL,
               tot VARCHAR NOT NULL
            );
    """)
    listaEscribir.append(nombreTabla)

escribirFichero(listaEscribir)
