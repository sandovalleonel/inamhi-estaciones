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
               fecha_archivo VARCHAR NOT NULL, 
               nom VARCHAR,
               resultado_00 VARCHAR ,
               tot_proce_00 VARCHAR,
               resultado_05 VARCHAR ,
               tot_proce_05 VARCHAR,
               resultado_10 VARCHAR ,
               tot_proce_10 VARCHAR,
               resultado_15 VARCHAR ,
               tot_proce_15 VARCHAR,
               resultado_20 VARCHAR ,
               tot_proce_20 VARCHAR,
               resultado_25 VARCHAR ,
               tot_proce_25 VARCHAR,
               resultado_30 VARCHAR ,
               tot_proce_30 VARCHAR,
               resultado_35 VARCHAR ,
               tot_proce_35 VARCHAR,
               resultado_40 VARCHAR ,
               tot_proce_40 VARCHAR,
               resultado_45 VARCHAR ,
               tot_proce_45 VARCHAR,
               resultado_50 VARCHAR ,
               tot_proce_50 VARCHAR,
               resultado_55 VARCHAR ,
               tot_proce_55 VARCHAR
               

            );
    """)
    listaEscribir.append(nombreTabla)

escribirFichero(listaEscribir)
